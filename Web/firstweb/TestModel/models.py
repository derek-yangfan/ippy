# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TestmodelContact(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'TestModel_contact'


class TestmodelTag(models.Model):
    name = models.CharField(max_length=50)
    contact = models.ForeignKey(TestmodelContact, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'TestModel_tag'


class TestmodelTest(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'TestModel_test'


class AclConnectionList(models.Model):
    acl_nr = models.IntegerField(blank=True, null=True)
    purpose = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    source = models.CharField(max_length=250, blank=True, null=True)
    src_vlan = models.CharField(max_length=10, blank=True, null=True)
    src = models.CharField(max_length=250, blank=True, null=True)
    src_mask = models.CharField(max_length=50, blank=True, null=True)
    src_port = models.CharField(max_length=500, blank=True, null=True)
    dst_vlan = models.CharField(max_length=10, blank=True, null=True)
    destination = models.CharField(max_length=250, blank=True, null=True)
    dst = models.CharField(max_length=250, blank=True, null=True)
    dst_mask = models.CharField(max_length=50, blank=True, null=True)
    application_protocol = models.CharField(max_length=100, blank=True, null=True)
    proto_id = models.CharField(max_length=20, blank=True, null=True)
    icmp_type = models.CharField(max_length=25, blank=True, null=True)
    bidirectional = models.CharField(max_length=1, blank=True, null=True)
    encrypted_base_proto = models.CharField(max_length=100, blank=True, null=True)
    remark = models.CharField(max_length=100, blank=True, null=True)
    client_id = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acl_connection_list'


class AclList(models.Model):
    src = models.CharField(max_length=15, blank=True, null=True)
    src_wmask = models.CharField(max_length=15, blank=True, null=True)
    src_port = models.CharField(max_length=75, blank=True, null=True)
    src_operator = models.CharField(max_length=5, blank=True, null=True)
    dst = models.CharField(max_length=15, blank=True, null=True)
    dst_wmask = models.CharField(max_length=15, blank=True, null=True)
    dst_port = models.CharField(max_length=75, blank=True, null=True)
    dst_operator = models.CharField(max_length=5, blank=True, null=True)
    proto_id = models.CharField(max_length=10, blank=True, null=True)
    action = models.CharField(max_length=6, blank=True, null=True)
    icmp_type = models.CharField(max_length=2, blank=True, null=True)
    client_id = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acl_list'


class Audit(models.Model):
    id = models.IntegerField(primary_key=True)
    event = models.CharField(max_length=500)
    user = models.CharField(max_length=50, blank=True, null=True)
    event_class = models.SmallIntegerField(blank=True, null=True)
    event_type = models.SmallIntegerField(blank=True, null=True)
    update_type_audit = models.SmallIntegerField(blank=True, null=True)
    date = models.BigIntegerField()
    client_id = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audit'


class AuditAuto(models.Model):
    event = models.CharField(max_length=500)
    user = models.CharField(max_length=50, blank=True, null=True)
    event_class = models.SmallIntegerField(blank=True, null=True)
    event_type = models.SmallIntegerField(blank=True, null=True)
    update_type_audit = models.SmallIntegerField(blank=True, null=True)
    date = models.BigIntegerField()
    client_id = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audit_auto'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AutonomousSystems(models.Model):
    as_number = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    comment = models.CharField(max_length=500, blank=True, null=True)
    as_client_id = models.SmallIntegerField(blank=True, null=True)
    client_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'autonomous_systems'


class AutonomousSystemsClients(models.Model):
    client_name = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    comment = models.CharField(max_length=500, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    fax = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    contact = models.CharField(max_length=500, blank=True, null=True)
    contact_email = models.CharField(max_length=100, blank=True, null=True)
    contact_phone = models.CharField(max_length=30, blank=True, null=True)
    contact_cell = models.CharField(max_length=30, blank=True, null=True)
    client_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'autonomous_systems_clients'


class Categorias(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    cat = models.CharField(unique=True, max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorias'


class CategoriasNet(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    cat = models.CharField(unique=True, max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorias_net'


class ClientEntries(models.Model):
    client_id = models.SmallIntegerField()
    phone = models.CharField(max_length=30, blank=True, null=True)
    fax = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    comment = models.CharField(max_length=500, blank=True, null=True)
    contact_name_1 = models.CharField(max_length=200, blank=True, null=True)
    contact_phone_1 = models.CharField(max_length=25, blank=True, null=True)
    contact_cell_1 = models.CharField(max_length=25, blank=True, null=True)
    contact_email_1 = models.CharField(max_length=50, blank=True, null=True)
    contact_comment_1 = models.CharField(max_length=500, blank=True, null=True)
    contact_name_2 = models.CharField(max_length=200, blank=True, null=True)
    contact_phone_2 = models.CharField(max_length=25, blank=True, null=True)
    contact_cell_2 = models.CharField(max_length=25, blank=True, null=True)
    contact_email_2 = models.CharField(max_length=50, blank=True, null=True)
    contact_comment_2 = models.CharField(max_length=500, blank=True, null=True)
    contact_name_3 = models.CharField(max_length=200, blank=True, null=True)
    contact_phone_3 = models.CharField(max_length=25, blank=True, null=True)
    contact_cell_3 = models.CharField(max_length=25, blank=True, null=True)
    contact_email_3 = models.CharField(max_length=50, blank=True, null=True)
    contact_comment_3 = models.CharField(max_length=500, blank=True, null=True)
    default_resolver = models.CharField(max_length=3, blank=True, null=True)
    dns_server_1 = models.CharField(max_length=50, blank=True, null=True)
    dns_server_2 = models.CharField(max_length=50, blank=True, null=True)
    dns_server_3 = models.CharField(max_length=50, blank=True, null=True)
    dns_server_1_key_name = models.CharField(max_length=50, blank=True, null=True)
    dns_server_2_key_name = models.CharField(max_length=50, blank=True, null=True)
    dns_server_3_key_name = models.CharField(max_length=50, blank=True, null=True)
    dns_server_1_key = models.CharField(max_length=100, blank=True, null=True)
    dns_server_2_key = models.CharField(max_length=100, blank=True, null=True)
    dns_server_3_key = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client_entries'


class Clients(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    client = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'clients'


class CmServer(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    ip = models.CharField(max_length=40)
    server_root = models.CharField(max_length=500)
    cm_server_type = models.CharField(max_length=10, blank=True, null=True)
    cm_server_description = models.CharField(max_length=500, blank=True, null=True)
    cm_server_username = models.CharField(max_length=100, blank=True, null=True)
    cm_server_password = models.CharField(max_length=100, blank=True, null=True)
    client_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cm_server'


class Config(models.Model):
    smallest_bm = models.SmallIntegerField(blank=True, null=True)
    max_sinc_procs = models.SmallIntegerField(blank=True, null=True)
    ignorar = models.CharField(max_length=250, blank=True, null=True)
    ignore_generic_auto = models.CharField(max_length=3, blank=True, null=True)
    generic_dyn_host_name = models.CharField(max_length=250, blank=True, null=True)
    set_sync_flag = models.CharField(max_length=3, blank=True, null=True)
    dyn_ranges_only = models.CharField(max_length=1, blank=True, null=True)
    ping_timeout = models.IntegerField(blank=True, null=True)
    confirmation = models.CharField(max_length=3, blank=True, null=True)
    client_id = models.SmallIntegerField(blank=True, null=True)
    smallest_bm6 = models.CharField(max_length=3, blank=True, null=True)
    ocs_enabled = models.CharField(max_length=3, blank=True, null=True)
    ocs_database_user = models.CharField(max_length=30, blank=True, null=True)
    ocs_database_name = models.CharField(max_length=30, blank=True, null=True)
    ocs_database_pass = models.CharField(max_length=30, blank=True, null=True)
    ocs_database_ip = models.CharField(max_length=42, blank=True, null=True)
    ocs_database_port = models.CharField(max_length=30, blank=True, null=True)
    ignore_dns = models.IntegerField(blank=True, null=True)
    confirm_dns_delete = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'config'


class CustomHostColumnEntries(models.Model):
    cc_id = models.SmallIntegerField()
    pc_id = models.SmallIntegerField()
    host_id = models.IntegerField()
    entry = models.CharField(max_length=10000)
    client_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'custom_host_column_entries'


class CustomHostColumns(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    column_type_id = models.IntegerField(blank=True, null=True)
    client_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'custom_host_columns'


class CustomNetColumnEntries(models.Model):
    cc_id = models.SmallIntegerField()
    net_id = models.SmallIntegerField()
    entry = models.CharField(max_length=150)
    client_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'custom_net_column_entries'


class CustomNetColumns(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    column_type_id = models.IntegerField(blank=True, null=True)
    client_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'custom_net_columns'


class CustomSiteColumnEntries(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    column_id = models.SmallIntegerField()
    site_id = models.SmallIntegerField()
    entry = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'custom_site_column_entries'


class CustomSiteColumns(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'custom_site_columns'


class DeviceCmConfig(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    host_id = models.IntegerField()
    device_type_group_id = models.SmallIntegerField()
    device_user_group_id = models.SmallIntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=100, blank=True, null=True)
    login_pass = models.CharField(max_length=100, blank=True, null=True)
    enable_pass = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    connection_proto = models.CharField(max_length=20, blank=True, null=True)
    connection_proto_args = models.CharField(max_length=20, blank=True, null=True)
    cm_server_id = models.CharField(max_length=20, blank=True, null=True)
    save_config_changes = models.SmallIntegerField(blank=True, null=True)
    last_backup_date = models.DateTimeField(blank=True, null=True)
    last_backup_status = models.SmallIntegerField(blank=True, null=True)
    last_backup_log = models.CharField(max_length=40, blank=True, null=True)
    client_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'device_cm_config'


class DeviceJobGroups(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True, null=True)
    client_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'device_job_groups'


class DeviceJobs(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    host_id = models.IntegerField()
    job_name = models.CharField(max_length=50, blank=True, null=True)
    job_group_id = models.SmallIntegerField(blank=True, null=True)
    job_descr = models.CharField(max_length=500, blank=True, null=True)
    job_type_id = models.SmallIntegerField(blank=True, null=True)
    last_execution_date = models.DateTimeField(blank=True, null=True)
    last_execution_status = models.SmallIntegerField(blank=True, null=True)
    last_execution_log = models.CharField(max_length=40, blank=True, null=True)
    enabled = models.SmallIntegerField(blank=True, null=True)
    client_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'device_jobs'


class DeviceKeys(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    comment = models.CharField(max_length=500)
    password = models.CharField(max_length=100)
    host_id = models.IntegerField(blank=True, null=True)
    client_id = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device_keys'


class DeviceUserGroups(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    login_pass = models.CharField(max_length=100)
    enable_pass = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True, null=True)
    client_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'device_user_groups'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DnsUser(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=50, blank=True, null=True)
    realm = models.CharField(max_length=60)
    description = models.CharField(max_length=1500)
    client_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'dns_user'


class DnsZone(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    dyn_dns_server = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    type = models.CharField(max_length=4, blank=True, null=True)
    dns_user_id = models.SmallIntegerField(blank=True, null=True)
    ttl = models.SmallIntegerField(blank=True, null=True)
    client_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'dns_zone'


class EventClasses(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    event_class = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_classes'


class EventTypes(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    event_type = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_types'


class GipUserGroupPerms(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    group_id = models.SmallIntegerField(blank=True, null=True)
    manage_gestioip_perm = models.IntegerField()
    manage_user_perm = models.IntegerField()
    manage_sites_and_cats_perm = models.IntegerField()
    manage_custom_columns_perm = models.IntegerField()
    read_audit_perm = models.IntegerField()
    clients_perm = models.CharField(max_length=100)
    cat_perm = models.CharField(max_length=200)
    loc_perm = models.CharField(max_length=200)
    create_net_perm = models.IntegerField()
    read_net_perm = models.IntegerField()
    update_net_perm = models.IntegerField()
    delete_net_perm = models.IntegerField()
    read_host_perm = models.IntegerField()
    create_host_perm = models.IntegerField()
    update_host_perm = models.IntegerField()
    delete_host_perm = models.IntegerField()
    read_vlan_perm = models.IntegerField()
    create_vlan_perm = models.IntegerField()
    update_vlan_perm = models.IntegerField()
    delete_vlan_perm = models.IntegerField()
    read_device_config_perm = models.IntegerField()
    write_device_config_perm = models.IntegerField()
    administrate_cm_perm = models.IntegerField()
    read_as_perm = models.IntegerField()
    create_as_perm = models.IntegerField()
    update_as_perm = models.IntegerField()
    delete_as_perm = models.IntegerField()
    read_line_perm = models.IntegerField()
    create_line_perm = models.IntegerField()
    update_line_perm = models.IntegerField()
    delete_line_perm = models.IntegerField()
    execute_update_dns_perm = models.IntegerField()
    execute_update_snmp_perm = models.IntegerField()
    execute_update_ping_perm = models.IntegerField()
    password_management_perm = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gip_user_group_perms'


class GipUserGroups(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gip_user_groups'


class GipUsers(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    group_id = models.SmallIntegerField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    comment = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gip_users'


class GlobalConfig(models.Model):
    version = models.CharField(max_length=10)
    default_client_id = models.CharField(max_length=150)
    confirmation = models.CharField(max_length=4)
    mib_dir = models.CharField(max_length=100, blank=True, null=True)
    vendor_mib_dirs = models.CharField(max_length=500, blank=True, null=True)
    ipv4_only = models.CharField(max_length=3, blank=True, null=True)
    as_enabled = models.CharField(max_length=3, blank=True, null=True)
    leased_line_enabled = models.CharField(max_length=3, blank=True, null=True)
    configuration_management_enabled = models.CharField(max_length=3, blank=True, null=True)
    cm_backup_dir = models.CharField(max_length=500, blank=True, null=True)
    cm_licence_key = models.CharField(max_length=500, blank=True, null=True)
    cm_log_dir = models.CharField(max_length=500, blank=True, null=True)
    cm_xml_dir = models.CharField(max_length=500, blank=True, null=True)
    auth_enabled = models.CharField(max_length=3, blank=True, null=True)
    freerange_ignore_non_root = models.IntegerField()
    arin_enabled = models.CharField(max_length=3, blank=True, null=True)
    local_filter_enabled = models.CharField(max_length=3)
    site_management_enabled = models.CharField(max_length=3)
    password_management_enabled = models.CharField(max_length=3, blank=True, null=True)
    dyn_dns_updates_enabled = models.CharField(max_length=3, blank=True, null=True)
    acl_management_enabled = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'global_config'


class Host(models.Model):
    ip = models.CharField(max_length=40, blank=True, null=True)
    hostname = models.CharField(max_length=100, blank=True, null=True)
    host_descr = models.CharField(max_length=100, blank=True, null=True)
    loc = models.SmallIntegerField(blank=True, null=True)
    red_num = models.IntegerField()
    categoria = models.SmallIntegerField(blank=True, null=True)
    int_admin = models.CharField(max_length=1, blank=True, null=True)
    comentario = models.CharField(max_length=500, blank=True, null=True)
    update_type = models.CharField(max_length=5, blank=True, null=True)
    last_update = models.BigIntegerField(blank=True, null=True)
    alive = models.IntegerField(blank=True, null=True)
    last_response = models.BigIntegerField(blank=True, null=True)
    range_id = models.SmallIntegerField(blank=True, null=True)
    ip_version = models.CharField(max_length=2, blank=True, null=True)
    dyn_dns_updates = models.SmallIntegerField(blank=True, null=True)
    client_id = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'host'


class Llines(models.Model):
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    comment = models.CharField(max_length=500, blank=True, null=True)
    loc = models.SmallIntegerField(blank=True, null=True)
    ll_client_id = models.SmallIntegerField(blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    service = models.CharField(max_length=100, blank=True, null=True)
    device = models.CharField(max_length=500, blank=True, null=True)
    room = models.CharField(max_length=500, blank=True, null=True)
    ad_number = models.CharField(max_length=100, blank=True, null=True)
    client_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'llines'


class LlinesClients(models.Model):
    client_name = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    comment = models.CharField(max_length=500, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    fax = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    contact = models.CharField(max_length=500, blank=True, null=True)
    contact_email = models.CharField(max_length=100, blank=True, null=True)
    contact_phone = models.CharField(max_length=30, blank=True, null=True)
    contact_cell = models.CharField(max_length=30, blank=True, null=True)
    client_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'llines_clients'


class Locations(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    loc = models.CharField(max_length=60, blank=True, null=True)
    client_id = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locations'


class MasterKeys(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    user_id = models.SmallIntegerField(blank=True, null=True)
    master_key = models.CharField(max_length=100)
    client_id = models.SmallIntegerField(blank=True, null=True)
    changed = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_keys'


class Net(models.Model):
    red = models.CharField(max_length=40, blank=True, null=True)
    bm = models.CharField(db_column='BM', max_length=3)  # Field name made lowercase.
    descr = models.CharField(max_length=100, blank=True, null=True)
    red_num = models.AutoField(primary_key=True)
    loc = models.SmallIntegerField()
    vigilada = models.CharField(max_length=1, blank=True, null=True)
    comentario = models.CharField(max_length=500, blank=True, null=True)
    categoria = models.SmallIntegerField(blank=True, null=True)
    ip_version = models.CharField(max_length=2, blank=True, null=True)
    rootnet = models.SmallIntegerField(blank=True, null=True)
    dyn_dns_updates = models.SmallIntegerField(blank=True, null=True)
    client_id = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'net'


class Ports(models.Model):
    port_nr = models.IntegerField()
    port_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'ports'


class PredefHostColumns(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'predef_host_columns'


class PredefNetColumns(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'predef_net_columns'


class Protocols(models.Model):
    protocol_nr = models.IntegerField()
    protocol_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'protocols'


class RangeType(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    range_type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'range_type'


class Ranges(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    start_ip = models.CharField(max_length=40)
    end_ip = models.CharField(max_length=40)
    comentario = models.CharField(max_length=50, blank=True, null=True)
    range_type = models.CharField(max_length=2, blank=True, null=True)
    red_num = models.CharField(max_length=5, blank=True, null=True)
    client_id = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ranges'


class UpdateType(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    type = models.CharField(unique=True, max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'update_type'


class UpdateTypesAudit(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    update_types_audit = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'update_types_audit'


class UserPasswords(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    password = models.CharField(max_length=100)
    user_id = models.SmallIntegerField()
    client_id = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_passwords'

"""
class VlanProviders(models.Model):
    id = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    comment = models.CharField(max_length=500, blank=True, null=True)
    client_id = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vlan_providers'
"""

class Vlans(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    vlan_num = models.CharField(max_length=10, blank=True, null=True)
    vlan_name = models.CharField(max_length=250, blank=True, null=True)
    comment = models.CharField(max_length=500, blank=True, null=True)
    provider_id = models.SmallIntegerField(blank=True, null=True)
    bg_color = models.CharField(max_length=20, blank=True, null=True)
    font_color = models.CharField(max_length=20, blank=True, null=True)
    switches = models.CharField(max_length=10000, blank=True, null=True)
    asso_vlan = models.SmallIntegerField(blank=True, null=True)
    client_id = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vlans'
