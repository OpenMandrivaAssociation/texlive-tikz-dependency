# revision 25156
# category Package
# catalog-ctan /graphics/pgf/contrib/tikz-dependency
# catalog-date 2012-01-19 19:15:33 +0100
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-tikz-dependency
Version:	1.1
Release:	7
Summary:	A library for drawing dependency graphs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-dependency
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-dependency.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-dependency.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a library that draws together existing
TikZ facilities to make a comfortable environment for drawing
dependency graphs. Basic facilities of the package include a
lot of styling facilities, to let you personalize the look and
feel of the graphs.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tikz-dependency/tikz-dependency.sty
%doc %{_texmfdistdir}/doc/latex/tikz-dependency/AUTHORS
%doc %{_texmfdistdir}/doc/latex/tikz-dependency/LICENSE
%doc %{_texmfdistdir}/doc/latex/tikz-dependency/README
%doc %{_texmfdistdir}/doc/latex/tikz-dependency/VERSION
%doc %{_texmfdistdir}/doc/latex/tikz-dependency/pgfmanual-en-macros.tex
%doc %{_texmfdistdir}/doc/latex/tikz-dependency/pgfmanual.code.tex
%doc %{_texmfdistdir}/doc/latex/tikz-dependency/pgfmanual.pdflinks.code.tex
%doc %{_texmfdistdir}/doc/latex/tikz-dependency/pgfmanual.prettyprinter.code.tex
%doc %{_texmfdistdir}/doc/latex/tikz-dependency/tikz-dependency-doc.pdf
%doc %{_texmfdistdir}/doc/latex/tikz-dependency/tikz-dependency-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 31 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 770310
- Update to latest upstream package

* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 756901
- Rebuild to reduce used resources

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 739661
- texlive-tikz-dependency
- texlive-tikz-dependency

