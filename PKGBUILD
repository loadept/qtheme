# Maintainer: loadept <loadept3 [at] gmail [dot] com>

pkgname=qtheme
pkgver=2.0.6
pkgrel=1
pkgdesc="Tool for management qtile desktop environment"
url='https://github.com/loadept/qtheme'
arch=('any')
license=('MIT')
depends=('python>=3.12' 'qtile' 'kitty' 'fastfetch')
makedepends=('python-installer')
source=(
	${pkgname}-${pkgver}-py3-none-any.whl::${url}/releases/download/v${pkgver}/qtheme-${pkgver}-py3-none-any.whl
)
sha512sums=('36345e0bdb0cfd2bd2cc12171c454763e906fa35576721e7c1554dbbad21ec32aa195fb5e0d241197372f2dad7253ebe2e78b03d55318a282a342f967ce47cc7')

package() {
	echo "Installing ${pkgname}-${pkgver} into ${pkgdir}"

	python -m installer --destdir="$pkgdir" "${srcdir}/${pkgname}-${pkgver}-py3-none-any.whl"

	install -Dm 644 $pkgdir/usr/lib/python3.*/site-packages/qtheme-${pkgver}.dist-info/licenses/LICENSE \
		"${pkgdir}"/usr/share/licenses/${pkgname}

	install -Dm 644 $pkgdir/usr/lib/python3.*/site-packages/qtheme-${pkgver}.dist-info/METADATA \
		"${pkgdir}"/usr/share/doc/${pkgname}
}
