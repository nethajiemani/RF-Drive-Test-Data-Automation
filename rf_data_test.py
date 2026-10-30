import pandas as pd

# 1. Load your drive test dataset
df = pd.read_csv('drive_test_data.csv')

# 2. Multi-metric filter for trouble spots (Day 6 review)
trouble_spots = df[(df['RSRP'] < -100) & (df['SINR'] < 5)].copy()

# 3. Export the weak coverage report (Day 6 review)
trouble_spots.to_csv('weak_coverage_report.csv', index=False)
print(f"Exported {len(trouble_spots)} trouble rows to weak_coverage_report.csv")

# 4. Handle missing PCI column in the sample data by creating a mock PCI column for testing
if 'PCI' not in trouble_spots.columns:
    # Assigning sample PCIs based on row index for demonstration
    trouble_spots['PCI'] = [101 if i % 2 == 0 else 202 for i in range(len(trouble_spots))]

# 5. Group by PCI to find top interference sources (Day 7 new logic)
pci_summary = trouble_spots['PCI'].value_counts().reset_index()
pci_summary.columns = ['PCI', 'Trouble_Count']

# 6. Export the PCI summary report
pci_summary.to_csv('pci_trouble_summary.csv', index=False)
print("Exported PCI summary report successfully!")
print("\nTop Problem PCIs:")
print(pci_summary.head())