# window.py
#
# Copyright 2022 mirkobrombin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundationat version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk, Gio, Adw

from ubuntu_smoother.models.preset import Preset
from ubuntu_smoother.models.config import Config
from ubuntu_smoother.utils.configurator import Configurator


@Gtk.Template(resource_path='/pm/mirko/UbuntuSmoother/gtk/window.ui')
class UbuntuSmootherWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'UbuntuSmootherWindow'

    carousel = Gtk.Template.Child()
    btn_start = Gtk.Template.Child()
    btn_save = Gtk.Template.Child()
    switch_snap = Gtk.Template.Child()
    switch_flatpak = Gtk.Template.Child()
    switch_apport = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__config = Config(
            snap=Preset.snap,
            flatpak=Preset.flatpak,
            apport=Preset.apport
        )
        self.__buiild_ui()
        self.__connect_signals()

    def __buiild_ui(self):
        self.switch_snap.set_active(Preset.snap)
        self.switch_flatpak.set_active(Preset.flatpak)
        self.switch_apport.set_active(Preset.apport)

    def __connect_signals(self):
        self.btn_start.connect('clicked', self.__on_btn_start_clicked)
        self.btn_save.connect('clicked', self.on_btn_save_clicked)
        self.switch_snap.connect('state-set', self.__on_switch_snap_state_set)
        self.switch_flatpak.connect(
            'state-set', self.__on_switch_flatpak_state_set)
        self.switch_apport.connect(
            'state-set', self.__on_switch_apport_state_set)

    def __on_btn_start_clicked(self, widget):
        index = int(self.carousel.get_position())
        next_page = self.carousel.get_nth_page(index + 1)
        self.carousel.scroll_to(next_page, True)

    def __on_switch_snap_state_set(self, widget, state):
        self.__config.snap = state

    def __on_switch_flatpak_state_set(self, widget, state):
        self.__config.flatpak = state

    def __on_switch_apport_state_set(self, widget, state):
        self.__config.apport = state

    def on_btn_save_clicked(self, widget):
        Configurator(self.__config, fake=True).apply()