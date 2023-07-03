%global pname LibreSprite
%global commit 6ffe8472194bf5d0a73b4b2cd7f6804d3c80aa0c

Name: libresprite
Version: 1.0
Release: %autorelease
Summary: Animated sprite editor & pixel art tool

License: GPL-2.0-only and MIT

URL: https://github.com/LibreSprite/%{repo}
Source0: %{url}/archive/%{commit}/%{pname}-%{commit}.tar.gz

# Bundled simpleini
%global si_commit 0687587cef1816a04307d632e517be9803bbdca6
Source2: https://github.com/aseprite/simpleini/archive/%{si_commit}/simpleini-%{si_commit}.tar.gz

# Bundled clip
%global clip_commit a65a9e543e9a270bb7c58789d15d027bbd8efb2a
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

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: freetype-devel
BuildRequires: giflib-devel
BuildRequires: gtest-devel
BuildRequires: libcurl-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: libpng-devel
BuildRequires: lua-devel
BuildRequires: nodejs-devel
BuildRequires: pixman-devel
BuildRequires: SDL2-devel
BuildRequires: SDL2_image-devel
BuildRequires: tinyxml-devel
BuildRequires: zlib-devel

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

%description
LibreSprite is a free and open source program for creating
and animating your sprites.

 - Real-time animation previews.
 - Onion skinning.
 - Multiple sprites can be edited at once.
 - Ready to use palettes, or make your own.
 - Sprites are composed of both layers & frames.
 - Tiled drawing mode, useful to draw patterns and textures.
 - Pixel precise tools like filled contour, polygon, shading mode, etc.
 - Several file types supported for your sprites and animations.

%prep
%autosetup -n %{pname}-%{commit}

pushd third_party
rm -rf duktape simpleini pixman
tar xzf %{SOURCE2}
mv simpleini-%{si_commit} simpleini
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
%cmake \
	-DUSE_SHARED_CURL=TRUE \
	-DUSE_SHARED_FREETYPE=TRUE \
	-DUSE_SHARED_GIFLIB=TRUE \
	-DUSE_SHARED_GTEST=TRUE \
	-DUSE_SHARED_JPEGLIB=TRUE \
	-DUSE_SHARED_LIBPNG=TRUE \
	-DWITH_WEBP_SUPPORT=TRUE -DUSE_SHARED_LIBWEBP=TRUE \
	-DUSE_SHARED_PIXMAN=TRUE \
	-DUSE_SHARED_TINYXML=TRUE \
	-DUSE_SHARED_ZLIB=TRUE

%cmake_build

%install
%cmake_install

for size in 16 32 48 64; do
	install -Dpm 0644 data/icons/ase${size}.png \
		%{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/%{name}.png
done

desktop-file-install \
	--dir=%{buildroot}%{_datadir}/applications/ \
	desktop/%{name}.desktop

install -Dpm 0644 -t %{buildroot}%{_metainfodir} desktop/%{name}.appdata.xml

%check
appstream-util validate-relax --nonet desktop/%{name}.appdata.xml

%files
%license LICENSE.txt
%doc docs/files/*.txt README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_metainfodir}/%{name}.appdata.xml

%changelog
%autochangelog
