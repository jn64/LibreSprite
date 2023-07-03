%global pname LibreSprite

%global commit        6ffe8472194bf5d0a73b4b2cd7f6804d3c80aa0c
%global commit_date   20230614
%global short_commit  %(c=%{commit}; echo ${c:0:7})
%global snapshot      %{commit_date}git%{short_commit}

# Bundled libs
# duktape
%global dt_commit     6f715553e706b61e611aa4ae8e6fe90626800dae
# simpleini
%global si_commit     0687587cef1816a04307d632e517be9803bbdca6
# clip
%global clip_commit   a65a9e543e9a270bb7c58789d15d027bbd8efb2a
# flic
%global flic_commit   65a6072fa0aa611c383b44d21b87d41e2ea8b523
# undo
%global undo_commit   f39b188e29d0f9adaa49c8705c0f492939d967a9
# observable
%global obs_commit    89c97405025c17fbce5b147aae86fe35b00f98e5

Name:           libresprite
Version:        1.1~dev^%{snapshot}
Release:        %autorelease
Summary:        Animated sprite editor & pixel art tool

License:        GPL-2.0-only and MIT

URL:            https://github.com/%{pname}/%{pname}
Source0:        %{url}/archive/%{commit}/%{pname}-%{commit}.tar.gz
Source1:        https://github.com/LibreSprite/duktape/archive/%{dt_commit}/duktape-%{dt_commit}.tar.gz
Source2:        https://github.com/aseprite/simpleini/archive/%{si_commit}/simpleini-%{si_commit}.tar.gz
Source11:       https://github.com/aseprite/clip/archive/%{clip_commit}/clip-%{clip_commit}.tar.gz
Source12:       https://github.com/aseprite/flic/archive/%{flic_commit}/flic-%{flic_commit}.tar.gz
Source13:       https://github.com/aseprite/undo/archive/%{undo_commit}/undo-%{undo_commit}.tar.gz
Source14:       https://github.com/dacap/observable/%{obs_commit}/observable-%{obs_commit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  giflib-devel
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(lua)
# V8 for nodejs 18 on F37/38
BuildRequires:  pkgconfig(v8-10.2)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(tinyxml)
BuildRequires:  pkgconfig(zlib)

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

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
tar xzf %{SOURCE1}
tar xzf %{SOURCE2}
mv duktape-%{dt_commit} duktape
mv simpleini-%{si_commit} simpleini
popd

pushd src
rm -rf clip flic undo observable allegro
tar xzf %{SOURCE11}
tar xzf %{SOURCE12}
tar xzf %{SOURCE13}
tar xzf %{SOURCE14}
mv clip-%{clip_commit} clip
mv flic-%{flic_commit} flic
mv undo-%{undo_commit} undo
mv observable-%{obs_commit} observable
popd

%build
%cmake \
	-DWITH_WEBP_SUPPORT=TRUE

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
