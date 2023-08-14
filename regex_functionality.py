"""Helper Module for RegEx / String Searches"""

import re


def is_nas_trade(message: str):
    """If message is related to NAS100,
       Returns a dict that will include 'asset', 'trade_side',
       and 'order_type' attributes else None.
    """
    DEPR_nas_case = "^NAS100 (BUY|SELL)([a-z ]*)$"
    nas_case = "(?P<asset>^NAS100) (?P<trade_side>(BUY|SELL))(?P<order_type>([a-z ]*)$)"
    m = re.search(nas_case, message, flags=re.IGNORECASE | re.MULTILINE)

    if m:
        # Standardize & Clean Return Data
        out_dict = {
                    "asset"      : str(m['asset']).upper(),
                    "trade_side" : str(m['trade_side']).upper(),
                    "order_type" : None if m['order_type'] == '' else str(m['order_type']).strip().upper()
            }
        
        return out_dict
    
    return None






if __name__ == "__main__":
    SAMPLE_MESSAGE = "FREEDOM GBP/XAU SIGNALS, [8/1/2023 10:36 AM]" + "\n" +\
                     "NAS100 SELL LIMIT" + "\n" +\
                     "ENTRY:15720" + "\n" +\
                     "SL:15750" + "\n" +\
                     "TP1:15700" + "\n" +\
                     "TP2:15680" + "\n" +\
                     "TP3:15660" + "\n" +\
                     "TP4: 15640"
    
    SAMPLE_MESSAGE2 = "FREEDOM GBP/XAU SIGNALS, [7/17/2023 4:22 PM]" + "\n" +\
                             "NAS100 BUY" + "\n" +\
                             "ENTRY:15645" + "\n" +\
                             "SL:15615" + "\n" +\
                             "TP1:15665" + "\n" +\
                             "TP2:15685" + "\n" +\
                             "TP3:15705" + "\n" +\
                             "TP4: 15725"
                     
    #print(SAMPLE_MESSAGE)

    print(is_nas_trade(SAMPLE_MESSAGE2))


    # Considerations:
    #  Sometimes lower case
    #  Sometimes no order type (limit/ stop) --> default to limit
    #      Or could be a message like "[asset] buy now"