import rumps
import block as blocker
import unblock as unblocker

class SpotifyBlocker(rumps.App):
    def __init__(self):
        super(SpotifyBlocker, self).__init__("Sp-block")
        self.menu = ["Block", "Unblock"]

    @rumps.clicked("Block")
    def block(self, _):
        blocker.block()
        """rumps.notification("Hosts file modified to block ads")"""

    @rumps.clicked("Unblock")
    def unblock(self, _):
        unblocker.unblock()
        """rumps.notification("Hosts file modified to block ads")"""

if __name__ == "__main__":
    SpotifyBlocker().run()