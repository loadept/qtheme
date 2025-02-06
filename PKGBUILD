# Maintainer: loadept <falcorgd [at] gmail [dot] com>

pkgname=qtheme
pkgver=1.5.1
pkgrel=1
pkgdesc="Tool for management qtile desktop environment"
url='https://github.com/loadept/qtheme'
arch=('any')
license=('MIT')
depends=('python>=3.12' 'qtile' 'kitty' 'fastfetch')
source=(${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz)
sha512sums=('d4ae9537158580990856efc5e0ead898582a5e9bb119ec64b16b3165ec236f34a68c7a9d07f20bec3fa247b1ded6aa4bfe6998f8070a5626842c710d1ef52202')

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
