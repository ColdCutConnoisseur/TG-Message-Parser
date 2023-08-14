import unittest

from regex_functionality import is_nas_trade

class TestRecognitionParsing(unittest.TestCase):

    def setUp(self):
        self.test_message1 = "FREEDOM GBP/XAU SIGNALS, [8/1/2023 10:36 AM]" + "\n" +\
                             "NAS100 SELL LIMIT" + "\n" +\
                             "ENTRY:15720" + "\n" +\
                             "SL:15750" + "\n" +\
                             "TP1:15700" + "\n" +\
                             "TP2:15680" + "\n" +\
                             "TP3:15660" + "\n" +\
                             "TP4: 15640"
        
        self.test_message2 = "FREEDOM GBP/XAU SIGNALS, [8/3/2023 11:26 AM]" + "\n" +\
                             "NAS100 SELL LIMIT" + "\n" +\
                             "ENTRY:15415" + "\n" +\
                             "SL:15445" + "\n" +\
                             "TP1:15395" + "\n" +\
                             "TP2:15375" + "\n" +\
                             "TP3:15355" + "\n" +\
                             "TP4: 15335"

        self.test_message3 = "FREEDOM GBP/XAU SIGNALS, [8/10/2023 8:31 AM]" + "\n" +\
                             "XAUUSD BUY STOP" + "\n" +\
                             "ENTRY: 1917.5" + "\n" +\
                             "SL:1914.5" + "\n" +\
                             "TP1:1919.5" + "\n" +\
                             "TP2:1921.5" + "\n" +\
                             "TP3:1923.5" + "\n" +\
                             "TP4:1925.5"
        
        self.test_message4 = "FREEDOM GBP/XAU SIGNALS, [7/17/2023 4:22 PM]" + "\n" +\
                             "NAS100 BUY" + "\n" +\
                             "ENTRY:15645" + "\n" +\
                             "SL:15615" + "\n" +\
                             "TP1:15665" + "\n" +\
                             "TP2:15685" + "\n" +\
                             "TP3:15705" + "\n" +\
                             "TP4: 15725"

        self.test_message5 = "FREEDOM GBP/XAU SIGNALS, [7/27/2023 12:16 PM]" + "\n" +\
                             "NAS100 SELL" + "\n" +\
                             "ENTRY:15696" + "\n" +\
                             "SL:15726" + "\n" +\
                             "TP1:15676" + "\n" +\
                             "TP2:15656" + "\n" +\
                             "TP3:15636" + "\n" +\
                             "TP4:15616"
        
        self.no_trade_side_message1 = "FREEDOM GBP/XAU SIGNALS, [7/27/2023 12:16 PM]" + "\n" +\
                                     "NAS100" + "\n" +\
                                     "ENTRY:15696"
        
        self.no_trade_side_message2 = "FREEDOM GBP/XAU SIGNALS, [7/27/2023 12:16 PM]" + "\n" +\
                                     "NAS100 LIMIT" + "\n" +\
                                     "ENTRY:15696"
        
        self.casing_message = "FREEDOM GBP/XAU SIGNALS, [8/1/2023 10:36 AM]" + "\n" +\
                              "NaS100 SelL lImiT" + "\n" +\
                              "ENTRY:15720" + "\n" +\
                              "SL:15750" + "\n" +\
                              "TP1:15700" + "\n" +\
                              "TP2:15680" + "\n" +\
                              "TP3:15660" + "\n" +\
                              "TP4: 15640"
        
    def test_casing(self):
        m_object = is_nas_trade(self.casing_message)
        m_asset = m_object['asset']
        m_order_side = m_object['trade_side']
        m_order_type = m_object['order_type']

        self.assertEqual(m_asset, 'NAS100')
        self.assertEqual(m_order_side, 'SELL')
        self.assertEqual(m_order_type, 'LIMIT')

    def test_only_asset_message(self):
        m_object = is_nas_trade(self.no_trade_side_message1)

        self.assertIsNone(m_object)

    def test_no_order_type(self):
        m_object = is_nas_trade(self.test_message4)
        m_asset = m_object['asset']
        m_order_side = m_object['trade_side']
        m_order_type = m_object['order_type']

        self.assertEqual(m_asset, 'NAS100')
        self.assertEqual(m_order_side, 'BUY')
        self.assertIsNone(m_order_type)

    def test_differing_asset(self):
        m_object = is_nas_trade(self.test_message3)

        self.assertIsNone(m_object)

    def test_only_order_type_no_side(self):
        pass


if __name__ == "__main__":
    unittest.main()
