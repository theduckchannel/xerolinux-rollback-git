pkgname=xerolinux-rollback-git
pkgver=r6.e691387
pkgrel=2
pkgdesc='Xerolinux Rollback Utility to snapshot using the layout proposed in the snapper arch wiki page https://wiki.archlinux.org/index.php/Snapper#Suggested_filesystem_layout'
arch=('any')
license=('GPL3')
url='https://github.com/theduckchannel/xerolinux-rollback'
depends=('coreutils' 'python' 'btrfs-progs', 'snapper', 'python-pyqt5', 'python-qdarkstyle', 'konsole')
optdepends=('doas: Automatic priv escalation'
            'sudo: Automatic priv escalation')
makedepends=('git')
provides=('xerolinux-rollback')
conflicts=('xerolinux-rollback')
backup=(etc/xerolinux-rollback.conf)
source=(git+"$url.git")
md5sums=('SKIP')

pkgver() {
	cd "xerolinux-rollback"
	printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
    cd "xerolinux-rollback"
    install -Dm644  "xerolinux-rollback.conf" -t "$pkgdir/etc/"
    install -Dm755  "xerolinux-rollback" -t "$pkgdir/usr/bin/"
}
