%define upstream_name    Task-Dist-Zilla
%define upstream_version 1.102470

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Task to install dist-zilla and all its plugins
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Task/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Dist::Zilla)
BuildRequires: perl(Dist::Zilla::Plugin::ApacheTest)
BuildRequires: perl(Dist::Zilla::Plugin::ArchiveRelease)
BuildRequires: perl(Dist::Zilla::Plugin::AutoPrereq)
BuildRequires: perl(Dist::Zilla::Plugin::AutoVersion)
BuildRequires: perl(Dist::Zilla::Plugin::AutoVersion::Relative)
BuildRequires: perl(Dist::Zilla::Plugin::Bugtracker)
BuildRequires: perl(Dist::Zilla::Plugin::BumpVersion)
BuildRequires: perl(Dist::Zilla::Plugin::BumpVersionFromGit)
BuildRequires: perl(Dist::Zilla::Plugin::CheckChangeLog)
BuildRequires: perl(Dist::Zilla::Plugin::CheckChangesTests)
BuildRequires: perl(Dist::Zilla::Plugin::CheckExtraTests)
BuildRequires: perl(Dist::Zilla::Plugin::CompileTests)
BuildRequires: perl(Dist::Zilla::Plugin::ConfirmRelease)
BuildRequires: perl(Dist::Zilla::Plugin::CopyTo)
BuildRequires: perl(Dist::Zilla::Plugin::CriticTests)
BuildRequires: perl(Dist::Zilla::Plugin::DistManifestTests)
BuildRequires: perl(Dist::Zilla::Plugin::ExecDir)
BuildRequires: perl(Dist::Zilla::Plugin::ExtraTests)
BuildRequires: perl(Dist::Zilla::Plugin::FakeRelease)
BuildRequires: perl(Dist::Zilla::Plugin::FatPacker)
BuildRequires: perl(Dist::Zilla::Plugin::FinderCode)
BuildRequires: perl(Dist::Zilla::Plugin::GatherDir)
BuildRequires: perl(Dist::Zilla::Plugin::Git)
BuildRequires: perl(Dist::Zilla::Plugin::Git::Check)
BuildRequires: perl(Dist::Zilla::Plugin::Git::Commit)
BuildRequires: perl(Dist::Zilla::Plugin::Git::Push)
BuildRequires: perl(Dist::Zilla::Plugin::Git::Tag)
BuildRequires: perl(Dist::Zilla::Plugin::GitVersionCheckCJM)
BuildRequires: perl(Dist::Zilla::Plugin::HasVersionTests)
BuildRequires: perl(Dist::Zilla::Plugin::Homepage)
BuildRequires: perl(Dist::Zilla::Plugin::InlineFiles)
BuildRequires: perl(Dist::Zilla::Plugin::InlineFilesMARCEL)
BuildRequires: perl(Dist::Zilla::Plugin::InstallGuide)
BuildRequires: perl(Dist::Zilla::Plugin::KwaliteeTests)
BuildRequires: perl(Dist::Zilla::Plugin::LatestPrereqs)
BuildRequires: perl(Dist::Zilla::Plugin::License)
BuildRequires: perl(Dist::Zilla::Plugin::LocaleMsgfmt)
BuildRequires: perl(Dist::Zilla::Plugin::MakeMaker)
BuildRequires: perl(Dist::Zilla::Plugin::MakeMaker::Awesome)
BuildRequires: perl(Dist::Zilla::Plugin::MakeMaker::SkipInstall)
BuildRequires: perl(Dist::Zilla::Plugin::Manifest)
BuildRequires: perl(Dist::Zilla::Plugin::ManifestSkip)
BuildRequires: perl(Dist::Zilla::Plugin::MatchManifest)
BuildRequires: perl(Dist::Zilla::Plugin::MetaConfig)
BuildRequires: perl(Dist::Zilla::Plugin::MetaJSON)
BuildRequires: perl(Dist::Zilla::Plugin::MetaNoIndex)
BuildRequires: perl(Dist::Zilla::Plugin::MetaProvides)
BuildRequires: perl(Dist::Zilla::Plugin::MetaProvides::Class)
BuildRequires: perl(Dist::Zilla::Plugin::MetaProvides::FromFile)
BuildRequires: perl(Dist::Zilla::Plugin::MetaProvides::Package)
BuildRequires: perl(Dist::Zilla::Plugin::MetaRecommends)
BuildRequires: perl(Dist::Zilla::Plugin::MetaResources)
BuildRequires: perl(Dist::Zilla::Plugin::MetaTests)
BuildRequires: perl(Dist::Zilla::Plugin::MetaYAML)
BuildRequires: perl(Dist::Zilla::Plugin::MinimumVersionTests)
BuildRequires: perl(Dist::Zilla::Plugin::ModuleBuild)
BuildRequires: perl(Dist::Zilla::Plugin::ModuleBuild::Custom)
BuildRequires: perl(Dist::Zilla::Plugin::ModuleInstall)
BuildRequires: perl(Dist::Zilla::Plugin::NextRelease)
BuildRequires: perl(Dist::Zilla::Plugin::PerlTidy)
BuildRequires: perl(Dist::Zilla::Plugin::PkgVersion)
BuildRequires: perl(Dist::Zilla::Plugin::PodCoverageTests)
BuildRequires: perl(Dist::Zilla::Plugin::PodLoom)
BuildRequires: perl(Dist::Zilla::Plugin::PodPurler)
BuildRequires: perl(Dist::Zilla::Plugin::PodSpellingTests)
BuildRequires: perl(Dist::Zilla::Plugin::PodSyntaxTests)
BuildRequires: perl(Dist::Zilla::Plugin::PodVersion)
BuildRequires: perl(Dist::Zilla::Plugin::PodWeaver)
BuildRequires: perl(Dist::Zilla::Plugin::PortabilityTests)
BuildRequires: perl(Dist::Zilla::Plugin::Prepender)
BuildRequires: perl(Dist::Zilla::Plugin::Prereq)
BuildRequires: perl(Dist::Zilla::Plugin::PruneCruft)
BuildRequires: perl(Dist::Zilla::Plugin::PruneFiles)
BuildRequires: perl(Dist::Zilla::Plugin::Readme)
BuildRequires: perl(Dist::Zilla::Plugin::ReadmeMarkdownFromPod)
BuildRequires: perl(Dist::Zilla::Plugin::ReportVersions)
BuildRequires: perl(Dist::Zilla::Plugin::Repository)
BuildRequires: perl(Dist::Zilla::Plugin::ShareDir)
BuildRequires: perl(Dist::Zilla::Plugin::Signature)
BuildRequires: perl(Dist::Zilla::Plugin::SynopsisTests)
BuildRequires: perl(Dist::Zilla::Plugin::TaskWeaver)
BuildRequires: perl(Dist::Zilla::Plugin::TemplateCJM)
BuildRequires: perl(Dist::Zilla::Plugin::TestRelease)
BuildRequires: perl(Dist::Zilla::Plugin::UnusedVarsTests)
BuildRequires: perl(Dist::Zilla::Plugin::UploadToCPAN)
BuildRequires: perl(Dist::Zilla::Plugin::VersionFromModule)
BuildRequires: perl(Dist::Zilla::Plugin::VersionFromPrev)
BuildRequires: perl(Dist::Zilla::Plugin::VersionFromPrev::Finder::Git::LastVersion)
BuildRequires: perl(Dist::Zilla::Plugin::VersionFromPrev::Style::Classic)
BuildRequires: perl(Dist::Zilla::PluginBundle::AVAR)
BuildRequires: perl(Dist::Zilla::PluginBundle::Basic)
BuildRequires: perl(Dist::Zilla::PluginBundle::CJM)
BuildRequires: perl(Dist::Zilla::PluginBundle::Classic)
BuildRequires: perl(Dist::Zilla::PluginBundle::FAYLAND)
BuildRequires: perl(Dist::Zilla::PluginBundle::FakeClassic)
BuildRequires: perl(Dist::Zilla::PluginBundle::Filter)
BuildRequires: perl(Dist::Zilla::PluginBundle::Git)
BuildRequires: perl(Dist::Zilla::PluginBundle::JQUELIN)
BuildRequires: perl(Dist::Zilla::PluginBundle::MARCEL)
BuildRequires: perl(Dist::Zilla::PluginBundle::PDONELAN)
BuildRequires: perl(Dist::Zilla::PluginBundle::RJBS)
BuildRequires: perl(English)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This task is merely a placeholder to pull all dist-zilla related modules in
one go.

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
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


