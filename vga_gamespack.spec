Summary:	Mines, Connect 4 and Othello games for the Linux VGA console
Summary(de.UTF-8):	Verschiedene Denkspiele für Linux SVGAlib
Summary(es.UTF-8):	Varios juegos de rompecabezas para Linux SVGAlib
Summary(pl.UTF-8):	Gry Mines, Connect 4 i Othello dla linuksowej konsoli VGA
Summary(pt_BR.UTF-8):	Vários jogos de quebra-cabeça para Linux SVGAlib
Summary(tr.UTF-8):	SVGAlib ile çalışan çeşitli zeka oyunları
Name:		vga_gamespack
Version:	1.4
Release:	13
License:	distributable
Group:		Applications/Games
Source0:	ftp://sunsite.unc.edu/pub/Linux/games/strategy/%{name}-%{version}.tgz
# Source0-md5:	1e661abad1710b35a7a17b58ef53305c
Patch0:		%{name}-misc.patch
BuildRequires:	svgalib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The vga_gamespack package contains three games for the Linux VGA
console: Mines, Connect 4, and Othello.

%description -l de.UTF-8
Eine Auswahl verschiedener Denkspiele für die Linux-Konsole unter
Verwendung der SVGAlib, unter anderem solche Favoriten wie Othello,
Minesweeper und Connect 4.

%description -l es.UTF-8
Varios juegos "mentales" para Linux usando SVGAlib. La selección
incluye algunos best-sellers como Othello, Minesweeper, y Connect 4.

%description -l fr.UTF-8
Jeux de réflexion pour la console Linux, utilisant SVGAlib. Inclus
Othello Démineur et Connect 4.

%description -l pl.UTF-8
Pakiet zawiera trzy gry dla linuksowej konsoli VGA: Mines, Connect 4 i
Othello.

%description -l pt_BR.UTF-8
Vários jogos "mentais" para o Linux usando SVGAlib. A seleção inclui
alguns best-sellers como Othello, Minesweeper, e Connect 4.

%description -l tr.UTF-8
SVGAlib kullanan konsol oyunları. Othello, mayın tarlası ve hedef 4
gibi sevilen oyunları içerir.

%prep
%setup -q -n %{name}
%patch -P0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPT_FLAGS="%{rpmcflags}" \
	LIBDIR=%{_libdir}/games

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=%{_libdir}/games

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/vga_connectN
%attr(755,root,root) %{_bindir}/vga_mines
%attr(755,root,root) %{_bindir}/vga_othello
%{_libdir}/games/Vga16font8x16
