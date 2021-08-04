# Dependencies
from flask import Flask, request, jsonify
from sklearn.externals import joblib
import traceback
import pandas as pd
import numpy as np

from flask import Flask, abort, jsonify, request
import numpy as np
import pickle as pickle
from sklearn.preprocessing import normalize
import json

# Your API definition
app = Flask(__name__)
model_columns=list(['DATA_DOUM0', 'DATA_DOUM1', 'DATA_DOUM2', 'DATA_GROSSM0',
       'DATA_GROSSM1', 'DATA_GROSSM2', 'DATA_MBSM0', 'DATA_MBSM1',
       'DATA_MBSM2', 'ALL_GROSS_AMTM0', 'ALL_GROSS_AMTM1', 'ALL_GROSS_AMTM2',
       'MPESA_GROSSM0', 'MPESA_GROSSM1', 'MPESA_GROSSM2', 'OTHER_GROSSM0',
       'OTHER_GROSSM1', 'OTHER_GROSSM2', 'SMS_QTYM0', 'SMS_QTYM1', 'SMS_QTYM2',
       'TUNUKIWA_GROSSM0', 'TUNUKIWA_GROSSM1', 'TUNUKIWA_GROSSM2',
       'VOICE_GROSSM0', 'VOICE_GROSSM1', 'VOICE_GROSSM2', 'VOIC_MINSM0',
       'VOIC_MINSM1', 'VOIC_MINSM2', 'ETU_RECHARGES_COUNTM0',
       'ETU_RECHARGES_COUNTM1', 'ETU_RECHARGES_COUNTM2',
       'ETU_RECHARGES_VALUEM0', 'ETU_RECHARGES_VALUEM1',
       'ETU_RECHARGES_VALUEM2', 'MPESA_RECHARGES_COUNTM0',
       'MPESA_RECHARGES_COUNTM1', 'MPESA_RECHARGES_COUNTM2',
       'MPESA_RECHARGES_VALUEM0', 'MPESA_RECHARGES_VALUEM1',
       'MPESA_RECHARGES_VALUEM2', 'OTHER_RECHARGES_COUNTM0',
       'OTHER_RECHARGES_COUNTM1', 'OTHER_RECHARGES_COUNTM2',
       'OTHER_RECHARGES_VALUEM0', 'OTHER_RECHARGES_VALUEM1',
       'OTHER_RECHARGES_VALUEM2', 'VOUCHER_RECHARGES_COUNTM0',
       'VOUCHER_RECHARGES_COUNTM1', 'VOUCHER_RECHARGES_COUNTM2',
       'VOUCHER_RECHARGES_VALUEM0', 'VOUCHER_RECHARGES_VALUEM1',
       'VOUCHER_RECHARGES_VALUEM2', 'etu_blacklistM0', 'etu_blacklistM1',
       'etu_blacklistM2', 'AGE', 'AON', 'GSMA_CLASS_FeaturePhone',
       'GSMA_CLASS_Handheld', 'GSMA_CLASS_Mobile Phone/Feature phone',
       'GSMA_CLASS_Smartphone', 'MARKET_SEGMENT_Discerning Professional',
       'MARKET_SEGMENT_Hustler', 'MARKET_SEGMENT_Mass',
       'MARKET_SEGMENT_Unclassified', 'MARKET_SEGMENT_Youth', 'INCOMING_SMSM0',
       'INCOMING_SMSM1', 'INCOMING_SMSM2', 'SMS_DOUM0', 'SMS_DOUM1',
       'SMS_DOUM2', 'SMS_GROSSM0', 'SMS_GROSSM1', 'SMS_GROSSM2', 'SMS_QTM0',
       'SMS_QTM1', 'SMS_QTM2', 'data_ratio_M2', 'gross_dropM2', 'data_drop_M2',
       'data_drop_M1', 'gross_dropM1', 'drop_ratioM2', 'drop_ratioM1',
       'rech_dropM2', 'data_drop_ratio_rech_dropM2', 'avg_data_revM1',
       'avg_data_revM2', 'avg_drop_change', 'MARKET_SEGMENT_0'])
file = open("./validate_model_january.pkl",'rb')
model2 = pickle.load(file)

@app.route('/', methods=['POST'])
def predict():
    if model2:
        try:
            json_ = request.json
            print(json_)
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=model_columns, fill_value=0)

            prediction = list(model2.predict(np.array(query)))

            return jsonify({'prediction': str(prediction)})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')

if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 80 # If you don't provide any port the port will be set to 9000

    app.run(host='0.0.0.0',port=port, debug=True)

import sys
reload(sys)
sys.setdefaultencoding("ISO-8859-1")
