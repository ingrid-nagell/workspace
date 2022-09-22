#Importerer csv-fil med chat som ble definert av regex som "Lukke sak" og vurdert om det er riktig klassifisering
relative_path = "../../data/skade_txt/skadesak_matches.xlsx"
df = pd.read_excel(relative_path, header=1)