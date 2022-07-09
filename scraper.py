from BP2P import get_data
from datetime import datetime
date = datetime.now().strftime('%Hh%Mm %d-%m-%Y')

buy = get_data(1, 10, 'USDT', 'MAD', 'BUY')
buy = buy.iloc[0]
buy['date'] = date
buy.to_json(f'DATA/USDT/BUY/{date}.json')

sell = get_data(1, 10, 'USDT', 'MAD', 'SELL')
sell = sell.iloc[0]
sell['date'] = date
sell.to_json(f'DATA/USDT/SELL/{date}.json')