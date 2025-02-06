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
sha512sums=('a956265dcb150f3af8898f925d6eb78f849a4fae14156a2083e0c5b0615204cbd0c6146d3b9f18cf5d6a8b4c777e652ae0316c5348c520036a53fd6170156083')

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
