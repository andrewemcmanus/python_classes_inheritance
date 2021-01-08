class Phone():
    # this is a phone class that can be used for inheritance:
    def __init__(self, phone_number, color):
        self.phone_number = phone_number
        self.color = color
    def __str__(self):
        return f"This phone belongs to {self.phone_number}"
    def call(self, other_number):
        print(f"Calling: {other_number}...")
    def text(self, other_number, message):
        print(f"Sending {message} to {other_number}")
    def open_app(self, app_name):
        print(f"Opening {app_name}")

# inheriting a class:
class Android(Phone):
    def __init__(self, phone_number, color):
        # phone number and color are connected above, need this:
        super().__init__(phone_number, color)
        self.passcode = None
        self.battery = 50

    def __str__(self):
        return f"Android phone that belongs to number {self.phone_number}"

    def set_passcode(self, passcode):
        self.passcode = passcode
    def view_battery_life(self):
        print(f"Battery Life: {self.battery}")
    def charge_phone(self, charging_amount):
        self.battery += charging_amount
        if self.battery > 100:
            self.battery = 100
    def set_passcode(self, passcode):
        self.passcode = passcode
    def unlock_phone(self, passcode):
        if passcode == self.passcode:
            print('Phone unlocked')

frank_phone = Android('888-777-3333', 'black')

frank_phone.view_battery_life()
frank_phone.charge_phone(40)
frank_phone.view_battery_life()
frank_phone.charge_phone(20)
frank_phone.view_battery_life()
frank_phone.call('400-500-4765')
frank_phone.open_app('Zoom')


class Galaxy(Android):
    def __init__(self, phone_number, passcode, color, size):
        super().__init__(phone_number, passcode, color, size)
        self.model = model
        self.feature = feature
    def __str__(self):
        return f"This Galaxy belongs to {self.phone_number}"
    def check_model(self):
        print(f"This is a Galaxy {self.model}")
    def add_feature(self, new_feature):
        self.feature = new_feature
        print(f"This Galaxy now has {self.feature}")
