import pandas as pd

def load_data():
    datasets = {
        'inventory': pd.read_csv('datasets/inventory_management_data.csv'),
        'logistics': pd.read_csv('datasets/logistics_shipment_data.csv'),
        'orders': pd.read_csv('datasets/orders_procurement_data.csv'),
        'quality': pd.read_csv('datasets/quality_control_data.csv'),
        'shop_floor': pd.read_csv('datasets/shop_floor_production_data.csv'),
        'vendors': pd.read_csv('datasets/vendor_supplier_data.csv')
    }
    
    # Combine data into one searchable text corpus
    corpus = ""
    for name, df in datasets.items():
        corpus += f"Dataset: {name}\n"
        corpus += df.head(20).to_string(index=False) + "\n\n"
    
    return corpus
