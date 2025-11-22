# Maintainer: loadept <loadept3 [at] gmail [dot] com>

pkgname=qtheme
pkgver=3.0.2
pkgrel=1
pkgdesc="Tool for management qtile desktop environment"
url='https://github.com/loadept/qtheme'
arch=('any')
license=('MIT')
depends=('python>=3.12' 'python-pydantic' 'qtile' 'kitty' 'fastfetch')
makedepends=('python-installer')
source=(
	${pkgname}-${pkgver}-py3-none-any.whl::${url}/releases/download/v${pkgver}/qtheme-${pkgver}-py3-none-any.whl
)
sha512sums=('af4858826ed6e25dcd0740b17d05e23e030827bc603f24f18b26cb836d3ec9265e4979e130715474337c8df9ccd04b322fe8ed8e8164681b8cd1d0892e26752f')

package() {
	python -m installer --destdir="$pkgdir" "${srcdir}/${pkgname}-${pkgver}-py3-none-any.whl"

	install -Dm 644 $pkgdir/usr/lib/python3.*/site-packages/qtheme-${pkgver}.dist-info/licenses/LICENSE \
		"${pkgdir}"/usr/share/licenses/${pkgname}

	install -Dm 644 $pkgdir/usr/lib/python3.*/site-packages/qtheme-${pkgver}.dist-info/METADATA \
		"${pkgdir}"/usr/share/doc/${pkgname}
}
