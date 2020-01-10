%define kmod_name		mpt3sas
%define kmod_vendor		redhat
%define kmod_driver_version	26.100.01.00_dup7.6
%define kmod_driver_epoch	%{nil}
%define kmod_rpm_release	3
%define kmod_kernel_version	3.10.0-957.el7
%define kmod_kernel_version_min	%{nil}
%define kmod_kernel_version_dep	%{nil}
%define kmod_kbuild_dir		drivers/scsi/mpt3sas
%define kmod_dependencies       %{nil}
%define kmod_dist_build_deps	%{nil}
%define kmod_build_dependencies	%{nil}
%define kmod_devel_package	0
%define kmod_install_path	extra/kmod-redhat-mpt3sas

%{!?dist: %define dist .el7_6}
%{!?make_build: %define make_build make}

%if "%{kmod_kernel_version_dep}" == ""
%define kmod_kernel_version_dep %{kmod_kernel_version}
%endif

%if "%{kmod_dist_build_deps}" == ""
%if (0%{?rhel} > 7) || (0%{?centos} > 7)
%define kmod_dist_build_deps redhat-rpm-config kernel-abi-whitelists elfutils-libelf-devel kernel-rpm-macros kmod
%else
%define kmod_dist_build_deps redhat-rpm-config kernel-abi-whitelists
%endif
%endif

Source0:	%{kmod_name}-%{kmod_vendor}-%{kmod_driver_version}.tar.bz2
# Source code patches
Patch0:	_RHEL7.6_e-stor_01-60_scsi_mpt3sas_switch_to_pci_alloc_irq_vectors.patch
Patch1:	_RHEL7.6_e-stor_02-60_scsi_mpt3sas_fix_an_out_of_bound_write.patch
Patch2:	_RHEL7.6_e-stor_03-60_scsi_mpt3sas_Add_nvme_device_support_in_slave_al.patch
Patch3:	_RHEL7.6_e-stor_04-60_scsi_mpt3sas_Recognize_and_act_on_iopriority_inf.patch
Patch4:	_RHEL7.6_e-stor_05-60_scsi_mpt3sas_SGL_to_PRP_Translation_for_I-Os_to_.patch
Patch5:	_RHEL7.6_e-stor_06-60_scsi_mpt3sas_Added_support_for_nvme_encapsulated.patch
Patch6:	_RHEL7.6_e-stor_07-60_scsi_mpt3sas_API_.s_to_support_NVMe_drive_additi.patch
Patch7:	_RHEL7.6_e-stor_08-60_scsi_mpt3sas_API.s_to_remove_nvme_drive_from_sml.patch
Patch8:	_RHEL7.6_e-stor_09-60_scsi_mpt3sas_Handle_NVMe_PCIe_device_related_eve.patch
Patch9:	_RHEL7.6_e-stor_10-60_scsi_mpt3sas_Set_NVMe_device_queue_depth_as_128.patch
Patch10:	_RHEL7.6_e-stor_11-60_scsi_mpt3sas_scan_and_add_nvme_device_after_cont.patch
Patch11:	_RHEL7.6_e-stor_12-60_scsi_mpt3sas_Add-Task-management-debug-info-for-.patch
Patch12:	_RHEL7.6_e-stor_13-60_scsi_mpt3sas_NVMe_drive_support_for_BTDHMAPPING_.patch
Patch13:	_RHEL7.6_e-stor_14-60_scsi_mpt3sas_Fix_nvme_drives_checking_for_tlr.patch
Patch14:	_RHEL7.6_e-stor_15-60_scsi_mpt3sas_Fix_sparse_warnings.patch
Patch15:	_RHEL7.6_e-stor_16-60_scsi_mpt3sas_Update_mpt3sas_driver_version.patch
Patch16:	_RHEL7.6_e-stor_17-60_scsi_mpt3sas_fix_dma_addr_t_casts.patch
Patch17:	_RHEL7.6_e-stor_18-60_scsi_mpt3sas_cleanup__scsih_pcie_enumeration_eve.patch
Patch18:	_RHEL7.6_e-stor_19-60_scsi_mpt3sas_remove_a_stray_KERN_INFO.patch
Patch19:	_RHEL7.6_e-stor_20-60_scsi_mpt3sas_Replace_PCI_pool_old_API.patch
Patch20:	_RHEL7.6_e-stor_21-60_scsi_mpt3sas_Remove_unused_variable_requeue_even.patch
Patch21:	_RHEL7.6_e-stor_22-60_scsi_mpt3sas_Proper_handling_of_set-clear_of_ATA.patch
Patch22:	_RHEL7.6_e-stor_23-60_scsi_mpt3sas_set_default_value_for_cb_idx.patch
Patch23:	_RHEL7.6_e-stor_24-60_scsi_mpt3sas_use_list_splice_init_.patch
Patch24:	_RHEL7.6_e-stor_25-60_scsi_mpt3sas_separate_out__base_recovery_check_.patch
Patch25:	_RHEL7.6_e-stor_26-60_scsi_mpt3sas_open-code__scsih_scsi_lookup_get_.patch
Patch26:	_RHEL7.6_e-stor_27-60_scsi_mpt3sas_Introduce_mpt3sas_get_st_from_smid_.patch
Patch27:	_RHEL7.6_e-stor_28-60_scsi_mpt3sas_check_command_status_before_attempt.patch
Patch28:	_RHEL7.6_e-stor_29-60_scsi_mpt3sas_always_use_first_reserved_smid_for_.patch
Patch29:	_RHEL7.6_e-stor_30-60_scsi_mpt3sas_simplify_task_management_functions.patch
Patch30:	_RHEL7.6_e-stor_31-60_scsi_mpt3sas_simplify_mpt3sas_scsi_issue_tm_.patch
Patch31:	_RHEL7.6_e-stor_32-60_scsi_mpt3sas_simplify__wait_for_commands_to_comp.patch
Patch32:	_RHEL7.6_e-stor_33-60_virtio_scsi_use_cmd_size.patch
Patch33:	_RHEL7.6_e-stor_34-60_scsi_mpt3sas_lockless_command_submission.patch
Patch34:	_RHEL7.6_e-stor_35-60_scsi_mpt3sas_make_function__get_st_from_smid_sta.patch
Patch35:	_RHEL7.6_e-stor_36-60_scsi_mpt3sas_fix_oops_in_error_handlers_after_sh.patch
Patch36:	_RHEL7.6_e-stor_37-60_scsi_mpt3sas_wait_for_and_flush_running_commands.patch
Patch37:	_RHEL7.6_e-stor_38-60_scsi_mpt3sas_Add_PCI_device_ID_for_Andromeda.patch
Patch38:	_RHEL7.6_e-stor_39-60_scsi_mpt3sas_Configure_reply_post_queue_depth,_D.patch
Patch39:	_RHEL7.6_e-stor_40-60_scsi_mpt3sas_Introduce_API_to_get_BAR0_mapped_bu.patch
Patch40:	_RHEL7.6_e-stor_41-60_scsi_mpt3sas_Introduce_Base_function_for_cloning.patch
Patch41:	_RHEL7.6_e-stor_42-60_scsi_mpt3sas_Introduce_function_to_clone_mpi_req.patch
Patch42:	_RHEL7.6_e-stor_43-60_scsi_mpt3sas_Introduce_function_to_clone_mpi_rep.patch
Patch43:	_RHEL7.6_e-stor_44-60_scsi_mpt3sas_clarify_mmio_pointer_types.patch
Patch44:	_RHEL7.6_e-stor_45-60_scsi_mpt3sas_Do_not_mark_fw_event_workqueue_as_W.patch
Patch45:	_RHEL7.6_e-stor_46-60_scsi_mpt3sas_fix_spelling_mistake__disbale_->_di.patch
Patch46:	_RHEL7.6_e-stor_47-60_scsi_mpt3sas_Bug_fix_for_big_endian_systems.patch
Patch47:	_RHEL7.6_e-stor_48-60_scsi_mpt3sas_Pre-allocate_RDPQ_Array_at_driver_b.patch
Patch48:	_RHEL7.6_e-stor_49-60_scsi_mpt3sas_Lockless_access_for_chain_buffers.patch
Patch49:	_RHEL7.6_e-stor_50-60_scsi_mpt3sas_Optimize_I-O_memory_consumption_in_.patch
Patch50:	_RHEL7.6_e-stor_51-60_scsi_mpt3sas_Enhanced_handling_of_Sense_Buffer.patch
Patch51:	_RHEL7.6_e-stor_52-60_scsi_mpt3sas_Added_support_for_SAS_Device_Discov.patch
Patch52:	_RHEL7.6_e-stor_53-60_scsi_mpt3sas_Increase_event_log_buffer_to_suppor.patch
Patch53:	_RHEL7.6_e-stor_54-60_scsi_mpt3sas_Allow_processing_of_events_during_d.patch
Patch54:	_RHEL7.6_e-stor_55-60_scsi_mpt3sas_Cache_enclosure_pages_during_enclos.patch
Patch55:	_RHEL7.6_e-stor_56-60_scsi_mpt3sas_Report_Firmware_Package_Version_fro.patch
Patch56:	_RHEL7.6_e-stor_57-60_scsi_mpt3sas_Update_MPI_Headers.patch
Patch57:	_RHEL7.6_e-stor_58-60_scsi_mpt3sas_For_NVME_device,_issue_a_protocol_l.patch
Patch58:	_RHEL7.6_e-stor_59-60_scsi_mpt3sas_fix_possible_memory_leak.patch
Patch59:	_RHEL7.6_e-stor_60-60_scsi_mpt3sas_Update_driver_version__25.100.00.00.patch
Patch60:	_RHEL-7.7_e-stor_61-60_scsi_mpt3sas_Fix_calltrace_observed_while_runni.patch
Patch61:	_RHEL-7.7_e-stor_62-60_scsi_mpt3sas_Add_an_I-O_barrier.patch
Patch62:	_RHEL-7.7_e-stor_63-60_scsi_mpt3sas_Swap_I-O_memory_read_value_back_to.patch
Patch63:	_RHEL-7.7_e-stor_01-36_scsi_mpt3sas_Don.t_abort_I-Os_issued_to_NVMe_dr.patch
Patch64:	_RHEL-7.7_e-stor_02-36_scsi_mpt3sas_Incorrect_command_status_was_set-m.patch
Patch65:	_RHEL-7.7_e-stor_03-36_scsi_mpt3sas_Don.t_access_the_structure_after_d.patch
Patch66:	_RHEL-7.7_e-stor_04-36_scsi_mpt3sas_Fix,_False_timeout_prints_for_ioct.patch
Patch67:	_RHEL-7.7_e-stor_05-36_scsi_mpt3sas_As_per_MPI-spec,_use_combined_repl.patch
Patch68:	_RHEL-7.7_e-stor_06-36_scsi_mpt3sas_Update_driver_version__26.100.00.0.patch
Patch69:	0070-bump-driver-version.patch
Patch70:	0071-remove-Andromeda-pci_id-from-supported.patch

%define findpat %( echo "%""P" )
%define __find_requires /usr/lib/rpm/redhat/find-requires.ksyms
%define __find_provides /usr/lib/rpm/redhat/find-provides.ksyms %{kmod_name} %{?epoch:%{epoch}:}%{version}-%{release}
%define sbindir %( if [ -d "/sbin" -a \! -h "/sbin" ]; then echo "/sbin"; else echo %{_sbindir}; fi )
%define dup_state_dir %{_localstatedir}/lib/rpm-state/kmod-dups
%define kver_state_dir %{dup_state_dir}/kver
%define kver_state_file %{kver_state_dir}/%{kmod_kernel_version}.%(arch)
%define dup_module_list %{dup_state_dir}/rpm-kmod-%{kmod_name}-modules

Name:		kmod-redhat-mpt3sas
Version:	%{kmod_driver_version}
Release:	%{kmod_rpm_release}%{?dist}
%if "%{kmod_driver_epoch}" != ""
Epoch:		%{kmod_driver_epoch}
%endif
Summary:	mpt3sas module for Driver Update Program
Group:		System/Kernel
License:	GPLv2
URL:		https://www.kernel.org/
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:	kernel-devel = %kmod_kernel_version
%if "%{kmod_dist_build_deps}" != ""
BuildRequires:	%{kmod_dist_build_deps}
%endif
ExclusiveArch:	x86_64 ppc64 ppc64le
%global kernel_source() /usr/src/kernels/%{kmod_kernel_version}.$(arch)

%global _use_internal_dependency_generator 0
%if "%{?kmod_kernel_version_min}" != ""
Provides:	kernel-modules >= %{kmod_kernel_version_min}.%{_target_cpu}
%else
Provides:	kernel-modules = %{kmod_kernel_version_dep}.%{_target_cpu}
%endif
Provides:	kmod-%{kmod_name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires(post):	%{sbindir}/weak-modules
Requires(postun):	%{sbindir}/weak-modules
Requires:	kernel >= 3.10.0-957.el7
Requires:	kernel < 3.10.0-958.el7
%if 0
Requires: firmware(%{kmod_name}) = ENTER_FIRMWARE_VERSION
%endif
%if "%{kmod_build_dependencies}" != ""
BuildRequires:  %{kmod_build_dependencies}
%endif
%if "%{kmod_dependencies}" != ""
Requires:       %{kmod_dependencies}
%endif
# if there are multiple kmods for the same driver from different vendors,
# they should conflict with each other.
Conflicts:	kmod-%{kmod_name}

%description
mpt3sas module for Driver Update Program

%if 0

%package -n kmod-redhat-mpt3sas-firmware
Version:	ENTER_FIRMWARE_VERSION
Summary:	mpt3sas firmware for Driver Update Program
Provides:	firmware(%{kmod_name}) = ENTER_FIRMWARE_VERSION
%if "%{kmod_kernel_version_min}" != ""
Provides:	kernel-modules >= %{kmod_kernel_version_min}.%{_target_cpu}
%else
Provides:	kernel-modules = %{kmod_kernel_version_dep}.%{_target_cpu}
%endif
%description -n  kmod-redhat-mpt3sas-firmware
mpt3sas firmware for Driver Update Program


%files -n kmod-redhat-mpt3sas-firmware
%defattr(644,root,root,755)
%{FIRMWARE_FILES}

%endif

# Development package
%if 0%{kmod_devel_package}
%package -n kmod-redhat-mpt3sas-devel
Version:	%{kmod_driver_version}
Requires:	kernel >= 3.10.0-957.el7
Requires:	kernel < 3.10.0-958.el7
Summary:	mpt3sas development files for Driver Update Program

%description -n  kmod-redhat-mpt3sas-devel
mpt3sas development files for Driver Update Program


%files -n kmod-redhat-mpt3sas-devel
%defattr(644,root,root,755)
/usr/share/kmod-%{kmod_vendor}-%{kmod_name}/Module.symvers
%endif

%post
modules=( $(find /lib/modules/%{kmod_kernel_version}.%(arch)/%{kmod_install_path} | grep '\.ko$') )
printf '%s\n' "${modules[@]}" | %{sbindir}/weak-modules --add-modules --no-initramfs

mkdir -p "%{kver_state_dir}"
touch "%{kver_state_file}"

exit 0

%posttrans
# We have to re-implement part of weak-modules here because it doesn't allow
# calling initramfs regeneration separately
if [ -f "%{kver_state_file}" ]; then
	kver_base="%{kmod_kernel_version_dep}"
	kvers=$(ls -d "/lib/modules/${kver_base%%.*}"*)

	for k_dir in $kvers; do
		k="${k_dir#/lib/modules/}"

		tmp_initramfs="/boot/initramfs-$k.tmp"
		dst_initramfs="/boot/initramfs-$k.img"

		# The same check as in weak-modules: we assume that the kernel present
		# if the symvers file exists.
		if [ -e "/boot/symvers-$k.gz" ]; then
			/usr/bin/dracut -f "$tmp_initramfs" "$k" || exit 1
			cmp -s "$tmp_initramfs" "$dst_initramfs"
			if [ "$?" = 1 ]; then
				mv "$tmp_initramfs" "$dst_initramfs"
			else
				rm -f "$tmp_initramfs"
			fi
		fi
	done

	rm -f "%{kver_state_file}"
	rmdir "%{kver_state_dir}" 2> /dev/null
fi

rmdir "%{dup_state_dir}" 2> /dev/null

exit 0

%preun
if rpm -q --filetriggers kmod 2> /dev/null| grep -q "Trigger for weak-modules call on kmod removal"; then
	mkdir -p "%{kver_state_dir}"
	touch "%{kver_state_file}"
fi

mkdir -p "%{dup_state_dir}"
rpm -ql kmod-redhat-mpt3sas-%{kmod_driver_version}-%{kmod_rpm_release}%{?dist}.$(arch) | \
	grep '\.ko$' > "%{dup_module_list}"

%postun
if rpm -q --filetriggers kmod 2> /dev/null| grep -q "Trigger for weak-modules call on kmod removal"; then
	initramfs_opt="--no-initramfs"
else
	initramfs_opt=""
fi

modules=( $(cat "%{dup_module_list}") )
rm -f "%{dup_module_list}"
printf '%s\n' "${modules[@]}" | %{sbindir}/weak-modules --remove-modules $initramfs_opt

rmdir "%{dup_state_dir}" 2> /dev/null

exit 0

%files
%defattr(644,root,root,755)
/lib/modules/%{kmod_kernel_version}.%(arch)
/etc/depmod.d/%{kmod_name}.conf
/usr/share/doc/kmod-%{kmod_name}/greylist.txt

%prep
%setup -n %{kmod_name}-%{kmod_vendor}-%{kmod_driver_version}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
set -- *
mkdir source
mv "$@" source/
mkdir obj

%build
rm -rf obj
cp -r source obj
%{make_build} -C %{kernel_source} V=1 M=$PWD/obj/%{kmod_kbuild_dir} \
	NOSTDINC_FLAGS="-I $PWD/obj/include -I $PWD/obj/include/uapi" \
	EXTRA_CFLAGS="%{nil}" \
	%{nil}
# mark modules executable so that strip-to-file can strip them
find obj/%{kmod_kbuild_dir} -name "*.ko" -type f -exec chmod u+x '{}' +

whitelist="/lib/modules/kabi-current/kabi_whitelist_%{_target_cpu}"
for modules in $( find obj/%{kmod_kbuild_dir} -name "*.ko" -type f -printf "%{findpat}\n" | sed 's|\.ko$||' | sort -u ) ; do
	# update depmod.conf
	module_weak_path=$(echo "$modules" | sed 's/[\/]*[^\/]*$//')
	if [ -z "$module_weak_path" ]; then
		module_weak_path=%{name}
	else
		module_weak_path=%{name}/$module_weak_path
	fi
	echo "override $(echo $modules | sed 's/.*\///')" \
	     "$(echo "%{kmod_kernel_version_dep}" |
	        sed 's/\.[^\.]*$//;
		     s/\([.+?^$\/\\|()\[]\|\]\)/\\\0/g').*" \
		     "weak-updates/$module_weak_path" >> source/depmod.conf

	# update greylist
	nm -u obj/%{kmod_kbuild_dir}/$modules.ko | sed 's/.*U //' |  sed 's/^\.//' | sort -u | while read -r symbol; do
		grep -q "^\s*$symbol\$" $whitelist || echo "$symbol" >> source/greylist
	done
done
sort -u source/greylist | uniq > source/greylist.txt

%install
export INSTALL_MOD_PATH=$RPM_BUILD_ROOT
export INSTALL_MOD_DIR=%{kmod_install_path}
make -C %{kernel_source} modules_install \
	M=$PWD/obj/%{kmod_kbuild_dir}
# Cleanup unnecessary kernel-generated module dependency files.
find $INSTALL_MOD_PATH/lib/modules -iname 'modules.*' -exec rm {} \;

install -m 644 -D source/depmod.conf $RPM_BUILD_ROOT/etc/depmod.d/%{kmod_name}.conf
install -m 644 -D source/greylist.txt $RPM_BUILD_ROOT/usr/share/doc/kmod-%{kmod_name}/greylist.txt
%if 0
%{FIRMWARE_FILES_INSTALL}
%endif
%if 0%{kmod_devel_package}
install -m 644 -D $PWD/obj/%{kmod_kbuild_dir}/Module.symvers $RPM_BUILD_ROOT/usr/share/kmod-%{kmod_vendor}-%{kmod_name}/Module.symvers
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Feb 06 2019 Eugene Syromiatnikov <esyr@redhat.com> 26.100.01.00_dup7.6-3
- Remove Andromeda PCI ID from the list of supported PCI IDs.

* Wed Jan 16 2019 Eugene Syromiatnikov <esyr@redhat.com> 26.100.01.00_dup7.6-1
- db1eefc8c25d0a3feaed310963bb3c3d04d81825
- Resolves: #bz1660390
- mpt3sas module for Driver Update Program
