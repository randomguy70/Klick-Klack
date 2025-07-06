import pandas as pd
import os

HOLD_MIN = 10
HOLD_MAX = 750

# compiles the data from either single csv or an entire directory of csv's into a single dataframe
# Opt: folder or file
def compile_data(fileOrFolder: str, path) -> pd.DataFrame:
    if fileOrFolder == 'folder':
        if path[len(path)-1] != '/':
            path += '/'
        files = [f for f in os.listdir(path)
        if f.endswith('.csv') and f != 'compiled.csv']
        
        dataframes = []
        for f in files:
            temp = pd.read_csv(path + f)
            dataframes.append(temp)
        
        df = pd.concat(dataframes, ignore_index=True)
    
    elif fileOrFolder == 'file':
        df = pd.read_csv(path)
    else:
        df = pd.DataFrame()
        
    df['key'] = df['key'].str.lower()
    return df
    
    
def extract_digraphs(df: pd.DataFrame, isPredictingSample: bool):
    rows = []
    for i in range(len(df) - 1):
        a = df.iloc[i]
        b = df.iloc[i + 1]
        if isPredictingSample or (a['participant'] == b['participant']):
            rows.append({
                'user': a['participant'],
                'key1': a['key'],
                'key2': b['key'],
                'Key1DownUP': float(a['hold_time']),
                'Key2DownUP': float(b['hold_time']),
                'Key1DownKey2Down': float(b['keydown_time']) - float(a['keydown_time']),
                'Key1UpKey2Up': float(b['keyup_time']) - float(a['keyup_time'])
            })
    return pd.DataFrame(rows)


# If we're extracting trigraphs from a sample that we're predicting on, we don't know the participant
def extract_trigraphs(df: pd.DataFrame, isPredictingSample: bool):
    rows = []
    for i in range(len(df) - 2):
        a, b, c = df.iloc[i], df.iloc[i + 1], df.iloc[i + 2]
        if isPredictingSample or (a['participant'] == b['participant'] == c['participant']):
            rows.append({
                'user': a['participant'],
                'key1': a['key'],
                'key2': b['key'],
                'key3': c['key'],
                'Key1DownUP': float(a['hold_time']),
                'Key2DownUP': float(b['hold_time']),
                'Key3DownUP': float(c['hold_time']),
                'Key1DownKey2Down': float(b['keydown_time']) - float(a['keydown_time']),
                'Key2DownKey3Down': float(c['keydown_time']) - float(b['keydown_time']),
                'Key1UpKey2Up': float(b['keyup_time']) - float(a['keyup_time']),
                'Key2UpKey3Up': float(c['keyup_time']) - float(b['keyup_time']),
                'Key1DownKey3Up': float(c['keyup_time']) - float(a['keydown_time'])
            })
    return pd.DataFrame(rows)


def apply_hold_time_filters_digraph(df, columns):
    """Filter out rows where any of the specified columns are outside the 10-750ms range. (Specified at top)"""
    condition = (
        (df['Key1DownUP'] >= HOLD_MIN) & (df['Key1DownUP'] <= HOLD_MAX) &
        (df['Key2DownUP'] >= HOLD_MIN) & (df['Key2DownUP'] <= HOLD_MAX)
    )
    
    return df[condition]


def apply_hold_time_filters_trigraph(df, columns):
    """Filter out rows where any of the specified columns are outside the 10-750ms range. (Specified at top)"""
    condition = (
        (df['Key1DownUP'] >= HOLD_MIN) & (df['Key1DownUP'] <= HOLD_MAX) &
        (df['Key2DownUP'] >= HOLD_MIN) & (df['Key2DownUP'] <= HOLD_MAX) &
        (df['Key3DownUP'] >= HOLD_MIN) & (df['Key3DownUP'] <= HOLD_MAX)
    )
    return df[condition]


def run(input_folder, output_folder):
    print("😐Compiling data files")
    df_all = compile_data('folder', input_folder)
    
    print("🙂Extracting digraphs...")
    digraph_df = extract_digraphs(df_all, isPredictingSample=False)
    digraph_df = apply_hold_time_filters_digraph(digraph_df, ['Key1DownUP', 'Key2DownUP'])
    digraph_df.to_csv(output_folder + 'digraph.csv', index=False)

    print("😁Extracting trigraphs...")
    trigraph_df = extract_trigraphs(df_all, isPredictingSample=False)
    trigraph_df = apply_hold_time_filters_digraph(trigraph_df, ['Key1DownUP', 'Key2DownUP', 'Key3DownUP'])
    trigraph_df.to_csv(output_folder + 'trigraph.csv', index=False)

    print("✅ Done! Digraphs and trigraphs saved.")