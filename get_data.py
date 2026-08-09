import os
import pandas as pd
import kagglehub

def main():
    print("🚀 Baixando o dataset do Kaggle...")
    
    path = kagglehub.dataset_download("yaminimanral/taylor-swift-dataset-ttpd-included")
    print(f"Pasta baixada em: {path}")

    csv_files = [f for f in os.listdir(path) if f.endswith('.csv')]
    
    if not csv_files:
        raise FileNotFoundError("Nenhum arquivo CSV encontrado no dataset baixado.")

    csv_path = os.path.join(path, csv_files[0])
    df = pd.read_csv(csv_path)

    print("\n✅ Dataset carregado com sucesso!")
    print(f"Total de músicas: {len(df)}")

    df.to_csv('taylor_swift_spotify.csv', index=False)
    print("📁 Arquivo 'taylor_swift_spotify.csv' criado com sucesso na raiz do seu projeto!")

if __name__ == '__main__':
    main()