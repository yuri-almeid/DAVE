import websocket
import json


'''proposal: 1,
			amount: 5,
			basis: "payout",
			contract_type: "DIGITODD",
			currency: "USD",
			duration: 1,
			duration_unit: "t",
			symbol: "R_50"

          json_data = json.dumps({'proposal': 1,
                            'amount': 5,
                            'basis': "payout",
                            'contract_type': "DIGITODD",
                            'currency': "USD",
                            'duration': 1,
                            'duration_unit': "t",
                            'symbol': "R_50"})
            '''


def on_open(ws):
    json_data = json.dumps({'buy' : '1aa5eade-1396-3ada-d469-6facceb4717b',
                            'price': 5})
    ws.send(json_data)

def on_message(ws, message):
    print('ticks update: %s' % message)

if __name__ == "__main__":
    apiUrl = "wss://ws.binaryws.com/websockets/v3?app_id=22566"
    ws = websocket.WebSocketApp(apiUrl, on_message = on_message, on_open = on_open)
    ws.run_forever()