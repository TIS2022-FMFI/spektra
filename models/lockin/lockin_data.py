import serial


class SerialConnectionData:
    def __init__(self, prt, bdr, bsz, par, stb, tim):
        self.port = prt
        self.baudrate = bdr
        self.bytesize = bsz
        self.parity = par
        self.stopbits = stb
        self.timeout = tim

    def getsettings(self):
        return self.port, self.baudrate, self.bytesize, self.parity, self.stopbits


sc = SerialConnectionData

lockin_data = {
    '_template': {
        'gain': [],
        'pre_time_const': [],
        'post_time_const': [],
        'serial_connection': None  # or sc(,,,,,,)
    }
}

with open('models/lockin/lockin_data.txt') as file:
    try:
        for line in file:
            name = line.strip()
            gain, pretc, postc, sercon = (eval(next(file)) for _ in range(4))

            lockin_data[name] = {
                'gain': gain,
                'pre_time_const': pretc,
                'post_time_const': postc,
                'serial_connection': None if sercon is None else sc(*sercon)
            }
    except Exception as e:
        print(e)
        print('wrong lockin_data.txt format')
