Summary:	Mines, Connect 4 and Othello games for the Linux VGA console
Summary(pl):	Gry Mines, Connect 4 i Othello dla linuksowej konsoli VGA
Name:		vga_gamespack
Version:	1.4
Release:	8
License:	distributable
Group:		Applications/Games
Group(cs):	Aplikace/Hry
Group(da):	Programmer/Spil
Group(de):	Applikationen/Spiele
Group(es):	Aplicaciones/Juegos
Group(fr):	Applications/Jeux
Group(is):	Forrit/Leikir
Group(it):	Applicazioni/Giochi
Group(ja):	•¢•◊•Í•±°º•∑•Á•Û/•≤°º•‡
Group(no):	Applikasjoner/Spill
Group(pl):	Aplikacje/Gry
Group(pt):	AplicaÁıes/Jogos
Group(ru):	“…Ãœ÷≈Œ…—/È«“Ÿ
Group(sl):	Programi/Igre
Group(sv):	Till‰mpningar/Spel
Group(uk):	“…ÀÃ¡ƒŒ¶ “œ«“¡Õ…/∂«“…
Source0:	ftp://sunsite.unc.edu/pub/Linux/games/strategy/%{name}-%{version}.tgz
Patch0:		%{name}-misc.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	svgalib-devel
ExclusiveArch:	%{ix86}

%description
The vga_gamespack package contains three games for the Linux VGA
console: Mines, Connect 4, and Othello.

%description -l pl
Pakiet zawiera trzy gry dla linuksowej konsoli VGA: Mines, Connect 4 i
Othello.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} CC="%{__cc}" OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/vga_connectN
%attr(755,root,root) %{_bindir}/vga_mines
%attr(755,root,root) %{_bindir}/vga_othello
%{_libdir}/games/Vga16font8x16
