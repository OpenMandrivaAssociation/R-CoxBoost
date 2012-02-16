%global packname  CoxBoost
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.2_1
Release:          1
Summary:          Cox models by likelihood based boosting for a single survival endpoint or competing risks
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/CoxBoost/index.html
Source0:          http://cran.r-project.org/src/contrib/Archive/CoxBoost/CoxBoost_1.2-1.tar.gz
Requires:         R-survival R-Matrix 
Requires:         R-snowfall R-multicore 
BuildRequires:    Rmath-devel texlive-collection-latex R-survival R-Matrix
BuildRequires:   R-snowfall R-multicore 
%rename R-cran-CoxBoost

%description
This package provides routines for fitting Cox models by likelihood based
boosting for a single endpoint or in presence of competing risks
%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
