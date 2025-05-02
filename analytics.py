import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def load_data():
    inventory = pd.read_csv('datasets/inventory_management_data.csv')
    orders = pd.read_csv('datasets/orders_procurement_data.csv')
    logistics = pd.read_csv('datasets/logistics_shipment_data.csv')
    quality = pd.read_csv('datasets/quality_control_data.csv')
    production = pd.read_csv('datasets/shop_floor_production_data.csv')
    vendors = pd.read_csv('datasets/vendor_supplier_data.csv')
    return inventory, orders, logistics, quality, production, vendors

def current_inventory_levels():
    inventory, _, _, _, _, _ = load_data()
    return inventory.groupby('Product')['Stock_Level'].sum().reset_index().to_json()

def predictive_inventory_shortage():
    inventory, orders, _, _, _, _ = load_data()

    # Aggregate orders by product clearly
    orders_summary = orders.groupby('Product')['Quantity'].sum().reset_index()

    # Merge inventory with orders clearly
    combined = pd.merge(inventory, orders_summary, on='Product', how='left').fillna(0)

    # Predictive analytics using Linear Regression explicitly
    model = LinearRegression()
    X = combined[['Stock_Level']]
    y = combined['Quantity']
    model.fit(X, y)

    # Predict future orders explicitly
    combined['Predicted_Next_Order'] = model.predict(X)
    combined['Shortage_Risk'] = combined['Stock_Level'] - combined['Predicted_Next_Order'] < 0

    return combined[['Product', 'Stock_Level', 'Predicted_Next_Order', 'Shortage_Risk']].to_json()
