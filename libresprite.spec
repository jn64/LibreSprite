Name: libresprite
Version: 1.0
Release: %autorelease
Summary: Pixel art editor

# LibreSprite itself is GPLv2.
# However, it depends on source code taken from:
#   duktape, simpleini, pixman, clip, flic, undo, observable
# which are subject to the MIT licence.
License: GPLv2 and MIT

%global repo LibreSprite
%global commit 0a01bb9a9d6cf65868cebc7f3df346044a6b1534

URL: https://github.com/LibreSprite/%{repo}
Source0: %{URL}/archive/%{commit}/%{repo}-%{commit}.tar.gz

# Bundled duktape
%global dt_commit 0de771cd55df729ec8a881b601ca3d4389e4a69a
Source1: https://github.com/aseprite/duktape/archive/%{dt_commit}/duktape-%{dt_commit}.tar.gz

# Bundled simpleini
%global si_commit 0687587cef1816a04307d632e517be9803bbdca6
Source2: https://github.com/aseprite/simpleini/archive/%{si_commit}/simpleini-%{si_commit}.tar.gz

# Bundled pixman
%global pm_commit 65f35270e4531621bd2e1ee5cdb31c56c3051c43
Source3: https://github.com/aseprite/pixman/archive/%{pm_commit}/pixman-%{pm_commit}.tar.gz

# Bundled clip
%global clip_commit 2f43c68f0dfe51fcdcbc9dcdbe6a62e24ddfd504
Source11: https://github.com/aseprite/clip/archive/%{clip_commit}/clip-%{clip_commit}.tar.gz

# Bundled flic
%global flic_commit 65a6072fa0aa611c383b44d21b87d41e2ea8b523
Source12: https://github.com/aseprite/flic/archive/%{flic_commit}/flic-%{flic_commit}.tar.gz

# Bundled undo
%global undo_commit f39b188e29d0f9adaa49c8705c0f492939d967a9
Source13: https://github.com/aseprite/undo/archive/%{undo_commit}/undo-%{undo_commit}.tar.gz

# Bundled observable
%global obs_commit 89c97405025c17fbce5b147aae86fe35b00f98e5
Source14: https://github.com/dacap/observable/%{obs_commit}/observable-%{obs_commit}.tar.gz

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: freetype-devel
BuildRequires: gcc-c++
BuildRequires: giflib-devel
BuildRequires: gtest-devel
BuildRequires: libappstream-glib
BuildRequires: libcurl-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: libpng-devel libwebp-devel
BuildRequires: libX11-devel libXcursor-devel
BuildRequires: ninja-build
BuildRequires: pixman-devel
BuildRequires: tinyxml-devel
BuildRequires: zlib-devel

Requires: hicolor-icon-theme

%description
LibreSprite lets you create 2D animations for videogames.
From sprites, to pixel-art, retro style graphics,
and whatever else you like about the 8-bit (and 16-bit) era.


%prep
%setup -q -n %{repo}-%{commit}

pushd third_party
rm -rf duktape simpleini pixman
tar xzf %{SOURCE1}
tar xzf %{SOURCE2}
tar xzf %{SOURCE3}
mv duktape-%{dt_commit} duktape
mv simpleini-%{si_commit} simpleini
mv pixman-%{pm_commit} pixman
popd

pushd src
rm -rf clip flic undo observable
tar xzf %{SOURCE11}
tar xzf %{SOURCE12}
tar xzf %{SOURCE13}
tar xzf %{SOURCE14}
mv clip-%{clip_commit} clip
mv flic-%{flic_commit} flic
mv undo-%{undo_commit} undo
mv observable-%{obs_commit} observable


%build
%set_build_flags
mkdir build && cd build
cmake \
  -DCMAKE_INSTALL_PREFIX=%{buildroot}%{_prefix} \
  -DUSE_SHARED_CURL=TRUE \
  -DUSE_SHARED_FREETYPE=TRUE \
  -DUSE_SHARED_GIFLIB=TRUE \
  -DUSE_SHARED_GTEST=TRUE \
  -DUSE_SHARED_JPEGLIB=TRUE \
  -DUSE_SHARED_LIBPNG=TRUE \
  -DWITH_WEBP_SUPPORT=TRUE -DUSE_SHARED_LIBWEBP=TRUE \
  -DUSE_SHARED_PIXMAN=TRUE \
  -DUSE_SHARED_TINYXML=TRUE \
  -DUSE_SHARED_ZLIB=TRUE \
  -G Ninja ..
ninja libresprite


%install
pushd build
ninja install 
popd

ICON_SIZES=`ls data/icons/ase*.png | sed -e 's|[^0-9]*||g'`
for SIZE in $ICON_SIZES; do
  SIZE_DIR="%{buildroot}%{_datadir}/icons/hicolor/${SIZE}x${SIZE}/apps/"
  install -m 755 -d "$SIZE_DIR"
  install -m 644 "data/icons/ase${SIZE}.png" "${SIZE_DIR}%{name}.png"
done

install -m 755 -d %{buildroot}%{_datadir}/applications/
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications/ \
  desktop/%{name}.desktop

appstream-util validate-relax --nonet desktop/%{name}.appdata.xml
install -m 755 -d %{buildroot}/%{_datadir}/appdata/
install -m 644 desktop/%{name}.appdata.xml %{buildroot}%{_datadir}/appdata/


%files
%license LICENSE.txt
%doc docs/ README.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/**/apps/%{name}.png

%changelog
%autochangelog
