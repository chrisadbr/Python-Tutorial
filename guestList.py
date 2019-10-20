class GuestList:

    def __init__(self, my_guests):
        self.guests = my_guests

    def all_guests_list(self):
        self.all_guests = []
        for guest in self.guests:
            self.all_guests.append(guest)

    def guests_invited(self, invited_guests):
            self.invitees = []
            for invited_guests in invited_guests:
                self.invitees.append(invited_guests)

    def display_invitees(self):
        print('\nList of guests:')
        for all_guests in self.guests:
            print(all_guests)
        print('\nList of VIP guests:')
        for vip_guest in self.invitees:
            print(vip_guest)


guest_list = []
vip_list = []
print('Guest list program enter quit once done with the list:')
while True:
    name = input('Enter the name of the guest: ').title()
    if name == 'Quit':
        print('Thank you a guests list has been received')
        break
    else:
        is_vip = input('VIP guest or regular guest (yes/no)').lower()
        if is_vip == 'yes':
            vip_list.append(name)
        elif is_vip == 'no':
            guest_list.append(name)


d1 = GuestList(guest_list)
# d1.all_guest_list()
d1.guests_invited(vip_list)
d1.display_invitees()
