import pandas as pd
import xgboost as xgb
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder


import pandas as pd
import joblib
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import os

def trainDigraphModel(
    csv_path,
    model_path,
    encoder_path,
    key_encoder_path,
    test_size=0.2,
    random_state=42
):
    # Load your digraph data
    digraph_df = pd.read_csv(csv_path)

    # Encode key1 and key2
    key1_encoder = LabelEncoder()
    key2_encoder = LabelEncoder()

    digraph_df['key1_encoded'] = key1_encoder.fit_transform(digraph_df['key1'])
    digraph_df['key2_encoded'] = key2_encoder.fit_transform(digraph_df['key2'])

    # Features include key1/key2 encodings and the numeric features
    feature_cols = [
        'Key1DownUP',
        'Key2DownUP',
        'Key1DownKey2Down',
        'Key1UpKey2Up',
        'key1_encoded',
        'key2_encoded'
    ]
    X = digraph_df[feature_cols]
    y = digraph_df['user']  # or 'participant'

    # Encode target labels (users)
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    # Split into train/test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=test_size, random_state=random_state, stratify=y_encoded
    )

    # Initialize XGBoost classifier
    model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')
    model.fit(X_train, y_train)

    # Predict and evaluate
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred, target_names=label_encoder.classes_))

    # Save model and encoders
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    model.save_model(model_path)
    joblib.dump(label_encoder, encoder_path)
    joblib.dump({'key1': key1_encoder, 'key2': key2_encoder}, key_encoder_path)

    print("✅ Model and encoders saved.")


def trainTrigraphModel(
    csv_path,
    model_path,
    encoder_path,
    key_encoder_path,
    test_size=0.2,
    random_state=42
):
    print("📦 Loading and preparing trigraph data...")
    df = pd.read_csv(csv_path)
    
    # Encode key1 and key2
    key1_encoder = LabelEncoder()
    key2_encoder = LabelEncoder()
    key3_encoder = LabelEncoder()
    
    df['key1_encoded'] = key1_encoder.fit_transform(df['key1'])
    df['key2_encoded'] = key2_encoder.fit_transform(df['key2'])
    df['key3_encoded'] = key3_encoder.fit_transform(df['key3'])
    
    # Features and label
    X = df.drop(columns=['user', 'key1', 'key2', 'key3'])
    y = df['user']
    
    # Encode the user labels
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=test_size, random_state=random_state
    )
    
    print("🧠 Training XGBoost model...")
    model = xgb.XGBClassifier(
        use_label_encoder=False,
        eval_metric='mlogloss',
        n_jobs=-1,
        verbosity=1
    )
    model.fit(X_train, y_train)
    
    # Evaluate
    print("📈 Evaluating model...")
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred, target_names=le.classes_))
    
    # Save model 
    print("💾 Saving model and label encoder...")
    model.save_model(model_path)
    
    # Save label encoder and class order
    joblib.dump(le, encoder_path)
    
    joblib.dump({'key1': key1_encoder, 'key2': key2_encoder, 'key3': key3_encoder}, key_encoder_path)

    print(f"✅ Training complete. Model saved to '{model_path}', encoder to '{encoder_path}'")
    return model, le


def full_train():
    print("Training Digraph Model")
    trainDigraphModel(
        csv_path='./Extracted_Data/digraph.csv',
        model_path='./models/digraph_model.json',
        encoder_path='./models/digraph_label_encoder.pkl',
        key_encoder_path='./models/digraph_key_encoder.pkl',
    )
    
    print("Trained Digraph Model")
    
    print("Training Trigraph Model")
    trainTrigraphModel(
        csv_path='./Extracted_Data/trigraph.csv',
        model_path='./models/trigraph_model.json',
        encoder_path='./models/trigraph_label_encoder.pkl',
        key_encoder_path='./models/trigraph_key_encoder.pkl',
    )
    print("Trained trigraph Model")
    