pkgname=xerolinux-rollback-git
pkgver=0.1.5
pkgrel=1
pkgdesc='Xerolinux Rollback Utility to snapshot using the layout proposed in the snapper arch wiki page https://wiki.archlinux.org/index.php/Snapper#Suggested_filesystem_layout'
arch=('any')
license=('GPL3')
url='https://github.com/theduckchannel/xerolinux-rollback'
depends=('coreutils' 'python' 'btrfs-progs', 'snapper', 'python-pyqt5', 'python-psutil','konsole', 'rollback-git', 'ttf-fira-code', 'python-elevate')
optdepends=()
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
    install -Dm755  "xerolinux-rollback" -t "$pkgdir/usr/bin/"
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
