from modules.smsmanager import Manager

manager = Manager("ACa986c0c89d8fde26628c01a0dccdb0ba", "77f00d3089824452f6bef85ee4452669", "5172009054")
print(manager.send_batch_message(["5174996430"], "Yo testing"))