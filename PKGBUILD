# Maintainer: loadept <falcorgd [at] gmail [dot] com>

pkgname=qtheme
pkgver=2.0.0
pkgrel=1
pkgdesc="Tool for management qtile desktop environment"
url='https://github.com/loadept/qtheme'
arch=('any')
license=('MIT')
depends=('python>=3.12' 'qtile' 'kitty' 'fastfetch')
source=(${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz)
sha512sums=('ee115d2b75cd999f4fc31b3e8dffa3a9c4311a8b203ef13f0006ae9d4ee0e93cdc23f6609656f611599f99d6566f059b3d554ff86cb53c3508ef2851a6476776')

build() {
	cd $pkgname-$pkgver
	python setup.py build
}

package() {
	cd $pkgname-$pkgver
	python setup.py install --prefix=/usr --root="${pkgdir}" -O1 --skip-build
	install -Dm 644 LICENSE -t "${pkgdir}"/usr/share/licenses/${pkgname}
	install -Dm 644 README.md -t "${pkgdir}"/usr/share/doc/${pkgname}
}
