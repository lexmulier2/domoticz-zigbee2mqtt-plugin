import Domoticz
from adopters.adopter import Adopter

class SensorWleak(Adopter):
    def create_device(self, unit, device_id, device_name, device_data):
        Domoticz.Debug('Creating dusk sensor for device with ieeeAddr ' + device_id)
        return Domoticz.Device(DeviceID=device_id, Name=device_name, Unit=unit, Type=244, Subtype=73, Switchtype=2).Create()

    def update_device(self, device, message):
        if ('water_leak' not in message):
            return

        water_leak = message['water_leak']
        signal_level = self.get_signal_level(message)
        battery_level = self.get_battery_level(message)

        if (battery_level == None):
            battery_level = device.BatteryLevel

        device.Update(nValue=1 if water_leak else 0, sValue='1' if water_leak else '0', SignalLevel=signal_level, BatteryLevel=battery_level)