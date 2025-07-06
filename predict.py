import pandas as pd
import xgboost as xgb
import joblib
import extract_data


def predict_top_users_from_trigraph(
    sample_data_path,
    model_path,
    key_encoder_path,
    label_encoder_path
):
    # Load trained model
    model = xgb.XGBClassifier()
    model.load_model(model_path)
    
    # Load key encoders
    label_encoder = joblib.load(label_encoder_path)
    class_labels = label_encoder.classes_
    
    key_encoders = joblib.load(key_encoder_path)

    # Load sample
    print("Extracting Trigraphs from Sample")
    sample_df = extract_data.compile_data('file', sample_data_path)
    sample_df = extract_data.extract_trigraphs(sample_df, isPredictingSample=True)

    # Encode key1, key2, key3
    for col in ['key1', 'key2', 'key3']:
        if col not in sample_df.columns:
            raise ValueError(f"Missing column '{col}' in the sample data.")
        if col not in key_encoders:
            raise ValueError(f"Missing encoder for key '{col}'.")
        sample_df[f'{col}_encoded'] = key_encoders[col].transform(sample_df[col])
        
    # Drop unused columns
    sample_df = sample_df.drop(columns=['participant', 'user', 'Session', 'key1', 'key2', 'key3'], errors='ignore')
    
    print("Filtering bad rows.")
    # Filter out bad rows
    # Important that we delete rows AFTER we load the trigraphs because the order in which
    # the keys were pressed is crucial to identifying trigraphs
    sample_df = extract_data.apply_hold_time_filters_trigraph(
        sample_df,
        ['Key1DownUP', 'Key2DownUP', 'Key3DownUP']
    )

    # Make sure all features used in training are present
    expected_columns = [
        'Key1DownUP', 'Key2DownUP', 'Key3DownUP',
        'Key1DownKey2Down', 'Key2DownKey3Down',
        'Key1UpKey2Up', 'Key2UpKey3Up', 'Key1DownKey3Up',
        'key1_encoded', 'key2_encoded', 'key3_encoded'
    ]
    missing_cols = set(expected_columns) - set(sample_df.columns)
    if missing_cols:
        raise ValueError(f"Missing required features: {missing_cols}")
    
    # Predict
    probabilities = model.predict_proba(sample_df)

    # Average predictions across all rows
    avg_probabilities = probabilities.mean(axis=0)

    # class_labels already has the correct mapping (index → username)
    prob_df = pd.DataFrame({
        'user': class_labels,
        'confidence_percent': (avg_probabilities * 100).round(2)
    })

    # Return top 2 predictions sorted by confidence
    return prob_df.sort_values(by='confidence_percent', ascending=False).head(2).reset_index(drop=True)


def predict_top_users_from_digraph(
    sample_data_path,
    model_path,
    key_encoder_path,
    label_encoder_path
):
    # Load trained model
    model = xgb.XGBClassifier()
    model.load_model(model_path)
    
    # Load key encoders
    label_encoder = joblib.load(label_encoder_path)
    class_labels = label_encoder.classes_
    
    key_encoders = joblib.load(key_encoder_path)

    # Load sample
    print("Extracting Digraphs from sample")
    sample_df = extract_data.compile_data('file', sample_data_path)
    sample_df = extract_data.extract_digraphs(sample_df, isPredictingSample=True)

    # Encode key1, key2, key3
    # Note, that keys present in a sample that the model wasn't trained on will cause an error.
    # Make sure the model is trained on at least several thousand keypresses for good performance. (A dozen typed paragraphs or so)
    for col in ['key1', 'key2']:
        if col not in sample_df.columns:
            raise ValueError(f"Missing column '{col}' in the sample data.")
        if col not in key_encoders:
            raise ValueError(f"Missing encoder for key '{col}'.")
        sample_df[f'{col}_encoded'] = key_encoders[col].transform(sample_df[col])
        
    # Drop unused columns
    sample_df = sample_df.drop(columns=['participant', 'user', 'Session', 'key1', 'key2'], errors='ignore')
    
    print("Filtering sample data")
    # Filter out bad rows
    sample_df = extract_data.apply_hold_time_filters_digraph(
        sample_df,
        ['Key1DownUP', 'Key2DownUP']
    )

    # Make sure all features used in training are present
    expected_columns = [
        'Key1DownUP', 'Key2DownUP', 'Key1DownKey2Down', 'Key1UpKey2Up',
        'key1_encoded', 'key2_encoded'
    ]
    missing_cols = set(expected_columns) - set(sample_df.columns)
    if missing_cols:
        raise ValueError(f"Missing required features: {missing_cols}")
    
    # Predict
    probabilities = model.predict_proba(sample_df)

    # Average predictions across all rows
    avg_probabilities = probabilities.mean(axis=0)

    # class_labels already has the correct mapping (index → username)
    prob_df = pd.DataFrame({
        'user': class_labels,
        'confidence_percent': (avg_probabilities * 100).round(2)
    })

    # Return top 2 predictions sorted by confidence
    return prob_df.sort_values(by='confidence_percent', ascending=False).head(2).reset_index(drop=True)


def getOverallPrediction(
    sample_data_path,
    trigraph_model_path,
    trigraph_key_encoder_path,
    trigraph_label_encoder_path,
    digraph_model_path,
    digraph_key_encoder_path,
    digraph_label_encoder_path
):
    trigraph_pred_df   = predict_top_users_from_trigraph(
        sample_data_path   = sample_data_path,
        model_path         = trigraph_model_path,
        key_encoder_path   = trigraph_key_encoder_path,
        label_encoder_path = trigraph_label_encoder_path
    )

    digraph_pred_df = predict_top_users_from_digraph (
        sample_data_path   = sample_data_path,
        model_path         = digraph_model_path,
        key_encoder_path   = digraph_key_encoder_path,
        label_encoder_path = digraph_label_encoder_path
    )
    
    trigraph_results = trigraph_pred_df.rename(columns={'confidence_percent': 'confidence_percent_trigraph'})
    digraph_results = digraph_pred_df.rename(columns={'confidence_percent': 'confidence_percent_digraph'})
    
    merged = pd.merge(digraph_results, trigraph_results, on='user')
    merged['Weighted Confidence'] = (merged['confidence_percent_digraph'] * 78 + merged['confidence_percent_trigraph'] * 90) / (78+90)

    return merged


######## Usage Example ########

prediction = getOverallPrediction(
    sample_data_path='./Test_Data/1234.csv',
    
    trigraph_model_path='./models/trigraph_model.json',
    trigraph_key_encoder_path='./models/trigraph_key_encoder.pkl',
    trigraph_label_encoder_path='./models/trigraph_label_encoder.pkl',
    
    digraph_model_path='./models/digraph_model.json',
    digraph_key_encoder_path='./models/digraph_key_encoder.pkl',
    digraph_label_encoder_path='./models/digraph_label_encoder.pkl'
)

print(prediction)