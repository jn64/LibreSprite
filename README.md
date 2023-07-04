# LibreSprite

RPM package of [LibreSprite](https://libresprite.github.io/) for Fedora

[![Copr build status badge](https://copr.fedorainfracloud.org/coprs/jn64/libresprite/package/libresprite/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/jn64/libresprite/)

## Install

```sh
sudo dnf copr enable jn64/libresprite
sudo dnf install libresprite
```

### Uninstall

```sh
sudo dnf remove libresprite
sudo dnf copr remove jn64/libresprite
```

## Build package locally

```sh
git clone -b rpm --single-branch https://github.com/jn64/LibreSprite.git libresprite
cd libresprite
spectool -g libresprite.spec
fedpkg --release f38 mockbuild
```

Find rpm(s) in `./results_libresprite/...`

## Release

```sh
fedpkg --release f38 srpm
copr-cli build --background jn64/libresprite <srpm>
```
