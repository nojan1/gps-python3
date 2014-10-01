# Maintainer: Niklas Hedlund <nojan1989@gmail.com>
pkgname=python-gps
pkgver=1
pkgrel=1
pkgdesc="Simple port of the standard Python2 "gps" package to Python3"
arch=(any)
url="https://github.com/nojan1/gps-python3"
license=('BSD')
groups=()
depends=('python')
makedepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=(!emptydirs)
install=("$pkgname:git+https://github.com/nojan1/gps-python3.git")
source=()
md5sums=('SKIP')

pkgver() {
  cd "$pkgname"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1
}

# vim:set ts=2 sw=2 et: