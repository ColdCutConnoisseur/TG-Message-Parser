"""Helper Module for RegEx / String Searches"""

import re


def is_nas_trade(message: str):
    """If message is related to NAS100,
       Returns a dict that will include 'asset', 'trade_side',
       and 'order_type' attributes else None.
    """
    nas_case = "(?P<asset>^NAS100) (?P<trade_side>(BUY|SELL))(?P<order_type>([a-z ]*)$)"
    m = re.search(nas_case, message, flags=re.IGNORECASE | re.MULTILINE)

    if not m:
        return None

    # Find Entry / Exit Prices
    entry_exp = "^ENTRY:[ ]?(?P<entry_px>[1-9]*$)"
    entry_px_m = re.search(entry_exp, message, flags=re.IGNORECASE | re.MULTILINE)

    # If entry price not found
    if not entry_px_m:
        return None
    
    # Find 'Stoploss'
    sl_exp = "^SL:[ ]?(?P<stoploss_px>[1-9]*$)"
    sl_px_m = re.search(sl_exp, message, flags=re.IGNORECASE | re.MULTILINE)

    if not sl_px_m:
        return None
    
    # Find 'TP1'
    tp1_exp = "^TP1:[ ]?(?P<tp1_px>[1-9]*$)"
    tp1_px_m = re.search(tp1_exp, message, flags=re.IGNORECASE | re.MULTILINE)

    if not tp1_px_m:
        return None
    
    # Find Remainder of TP Levels; they are not necessary for a trade to occur however
    # Find 'TP2'
    tp2_exp = "^TP2:[ ]?(?P<tp2_px>[1-9]*$)"
    tp2_px_m = re.search(tp2_exp, message, flags=re.IGNORECASE | re.MULTILINE)

    # Find 'TP3'
    tp3_exp = "^TP3:[ ]?(?P<tp3_px>[1-9]*$)"
    tp3_px_m = re.search(tp3_exp, message, flags=re.IGNORECASE | re.MULTILINE)

    # Find 'TP4'
    tp4_exp = "^TP4:[ ]?(?P<tp4_px>[1-9]*$)"
    tp4_px_m = re.search(tp4_exp, message, flags=re.IGNORECASE | re.MULTILINE)

    # Standardize & Clean Return Data
    out_dict = {
                "asset"       : str(m['asset']).upper(),
                "trade_side"  : str(m['trade_side']).upper(),
                "order_type"  : 'LIMIT' if m['order_type'] == '' else str(m['order_type']).strip().upper(),
                "entry_px"    : float(entry_px_m['entry_px']),
                "stoploss_px" : float(sl_px_m['stoploss_px']),
                "tp1_px"      : float(tp1_px_m['tp1_px']),
                "tp2_px"      : None if not tp2_px_m else float(tp2_px_m['tp2_px']),
                "tp3_px"      : None if not tp3_px_m else float(tp3_px_m['tp3_px']),
                "tp4_px"      : None if not tp4_px_m else float(tp4_px_m['tp4_px'])
        }
    
    # DEBUG
    print(out_dict['tp2_px'])
    
    return out_dict




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