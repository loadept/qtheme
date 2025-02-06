# Maintainer: loadept <falcorgd [at] gmail [dot] com>

pkgname=qtheme
pkgver=1.5.1
pkgrel=1
pkgdesc="Tool for management qtile desktop environment"
url='https://github.com/loadept/qtheme'
arch=('any')
license=('MIT')
depends=('python>=3.12' 'qtile' 'kitty' 'fastfetch')
source=(${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('9f44978cf5381ff31c9fad804e680b24451e1da9f8f9fb6c891f43d925635fce6f9f7bed335c10d0e0b5faa7f5d2f4faa059d173a4b8961e81751dfe1087becb')

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
