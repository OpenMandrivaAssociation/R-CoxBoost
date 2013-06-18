%global packname  CoxBoost
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.3
Release:          3
Summary:          Cox models by likelihood based boosting
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-survival R-Matrix R-snowfall R-multicore
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-survival
BuildRequires:    R-Matrix R-snowfall R-multicore
%rename R-cran-CoxBoost

%description
This package provides routines for fitting Cox models by likelihood based
boosting for a single endpoint or in presence of competing risks

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
