%define upstream_name    Dist-Zilla-PluginBundle-KENTNL
%define upstream_version 0.01017322

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Generate a C<dist.ini> for @KENTNL projects
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Dist::Zilla)
BuildRequires: perl(Dist::Zilla::File::FromCode)
BuildRequires: perl(Dist::Zilla::Plugin::AutoPrereq)
BuildRequires: perl(Dist::Zilla::Plugin::AutoVersion::Relative)
BuildRequires: perl(Dist::Zilla::Plugin::CompileTests)
BuildRequires: perl(Dist::Zilla::Plugin::ConfirmRelease)
BuildRequires: perl(Dist::Zilla::Plugin::CriticTests)
BuildRequires: perl(Dist::Zilla::Plugin::EOLTests)
BuildRequires: perl(Dist::Zilla::Plugin::ExtraTests)
BuildRequires: perl(Dist::Zilla::Plugin::FakeRelease)
BuildRequires: perl(Dist::Zilla::Plugin::GatherDir)
BuildRequires: perl(Dist::Zilla::Plugin::Git::Check)
BuildRequires: perl(Dist::Zilla::Plugin::Git::CommitBuild)
BuildRequires: perl(Dist::Zilla::Plugin::Git::Tag)
BuildRequires: perl(Dist::Zilla::Plugin::GithubMeta)
BuildRequires: perl(Dist::Zilla::Plugin::KwaliteeTests)
BuildRequires: perl(Dist::Zilla::Plugin::License)
BuildRequires: perl(Dist::Zilla::Plugin::Manifest)
BuildRequires: perl(Dist::Zilla::Plugin::ManifestSkip)
BuildRequires: perl(Dist::Zilla::Plugin::MetaConfig)
BuildRequires: perl(Dist::Zilla::Plugin::MetaData::BuiltWith)
BuildRequires: perl(Dist::Zilla::Plugin::MetaJSON)
BuildRequires: perl(Dist::Zilla::Plugin::MetaProvides)
BuildRequires: perl(Dist::Zilla::Plugin::MetaProvides::Package)
BuildRequires: perl(Dist::Zilla::Plugin::MetaTests)
BuildRequires: perl(Dist::Zilla::Plugin::MetaYAML)
BuildRequires: perl(Dist::Zilla::Plugin::ModuleBuild)
BuildRequires: perl(Dist::Zilla::Plugin::PkgVersion)
BuildRequires: perl(Dist::Zilla::Plugin::PodCoverageTests)
BuildRequires: perl(Dist::Zilla::Plugin::PodSyntaxTests)
BuildRequires: perl(Dist::Zilla::Plugin::PodWeaver)
BuildRequires: perl(Dist::Zilla::Plugin::PortabilityTests)
BuildRequires: perl(Dist::Zilla::Plugin::PruneCruft)
BuildRequires: perl(Dist::Zilla::Plugin::ReadmeFromPod)
BuildRequires: perl(Dist::Zilla::Plugin::ReportVersions::Tiny)
BuildRequires: perl(Dist::Zilla::Plugin::TestRelease)
BuildRequires: perl(Dist::Zilla::Plugin::Twitter)
BuildRequires: perl(Dist::Zilla::Plugin::UploadToCPAN)
BuildRequires: perl(Dist::Zilla::Role::FileGatherer)
BuildRequires: perl(Dist::Zilla::Role::PluginBundle)
BuildRequires: perl(English)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Temp)
BuildRequires: perl(IO::Socket::SSL)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Moose)
BuildRequires: perl(Moose::Autobox)
BuildRequires: perl(MooseX::Has::Sugar)
BuildRequires: perl(MooseX::Types)
BuildRequires: perl(Net::SSLeay)
BuildRequires: perl(Pod::Coverage::TrustPod)
BuildRequires: perl(String::Formatter)
BuildRequires: perl(Test::CPAN::Meta)
BuildRequires: perl(Test::EOL)
BuildRequires: perl(Test::More)
BuildRequires: perl(namespace::autoclean)
BuildRequires: perl(Module::Build)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This is the plug-in bundle that KENTNL uses. It exists mostly because he is
very lazy and wants others to be using what he's using if they want to be
doing work on his modules.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor

./Build

%check
./Build test

%install
rm -rf %buildroot
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE META.json META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


