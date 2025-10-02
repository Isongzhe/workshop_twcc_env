import intake 

def main():
    # Load the radar data catalog
    catalog = intake.open_catalog('./radar_intake_catalog.yaml')
    radar_tw_ds = catalog.QPESUMS_tw.to_dask()
    print(radar_tw_ds)

if __name__ == "__main__":
    main()
