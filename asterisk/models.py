from django.db import models


class Extentions(models.Model):
    context = models.CharField(max_length=30, default='phones', editable=False)
    exten = models.CharField(max_length=30, unique=True)
    priority = models.CharField(max_length=30, default='1', editable=False)
    app = models.CharField(max_length=30, default='AGI', editable=False)
    appdata = models.CharField(
        blank=True, max_length=30, default='testphp.php', editable=False)
    file = models.FileField(null=True)


class Queue(models.Model):
    name = models.CharField(max_length=128, primary_key=True)
    exten = models.CharField(max_length=128, null=True)
    optin = models.BigIntegerField(default=1)
    musiconhold = models.CharField(
        max_length=128, blank=True, null=True, default='phones', editable=False)
    announce = models.CharField(
        max_length=128, blank=True, null=True, editable=False)
    context = models.CharField(
        max_length=128, blank=True, null=True, editable=False)
    timeout = models.BigIntegerField(blank=True, null=True, editable=False)
    monitor_join = models.IntegerField(blank=True, null=True, editable=False)
    monitor_format = models.CharField(
        max_length=128, blank=True, null=True, editable=False)
    queue_youarenext = models.CharField(
        max_length=128, blank=True, null=True, editable=False)
    queue_thereare = models.CharField(
        max_length=128, blank=True, editable=False)
    queue_callswaiting = models.CharField(
        max_length=128, blank=True, null=True, editable=False)
    queue_holdtime = models.CharField(
        max_length=128, blank=True, null=True, editable=False)
    queue_minutes = models.CharField(
        max_length=128, blank=True, null=True, editable=False)
    queue_seconds = models.CharField(
        max_length=128, blank=True, null=True, editable=False)
    queue_lessthan = models.CharField(
        max_length=128, blank=True, null=True, editable=False)
    queue_thankyou = models.CharField(
        max_length=128, blank=True, null=True, editable=False)
    queue_reporthold = models.CharField(
        max_length=128, blank=True, null=True, editable=False)
    announce_frequency = models.BigIntegerField(
        blank=True, null=True, editable=False)
    announce_round_seconds = models.BigIntegerField(
        blank=True, null=True, editable=False)
    announce_holdtime = models.CharField(
        max_length=128, blank=True, null=True, editable=False)
    retry = models.BigIntegerField(blank=True, null=True, editable=False)
    wrapuptime = models.BigIntegerField(blank=True, null=True, editable=False)
    maxlen = models.BigIntegerField(blank=True, null=True, editable=False)
    servicelevel = models.BigIntegerField(
        blank=True, null=True, editable=False)
    strategy = models.CharField(
        max_length=30, blank=True, null=True, editable=False)
    joinempty = models.CharField(max_length=30, null=True, editable=False)
    leavewhenempty = models.CharField(
        max_length=30, blank=True, null=True, editable=False)
    eventmemberstatus = models.BigIntegerField(
        blank=True, null=True, editable=False)
    eventwhencalled = models.CharField(
        max_length=30, blank=True, null=True, editable=False)
    reportholdtime = models.BigIntegerField(
        blank=True, null=True, editable=False)
    memberdelay = models.BigIntegerField(blank=True, null=True, editable=False)
    weight = models.BigIntegerField(blank=True, null=True, editable=False)
    timeoutrestart = models.BigIntegerField(
        blank=True, null=True, editable=False)


class QueueMember(models.Model):
    uniqueid = models.BigIntegerField(primary_key=True, editable=False)
    membername = models.CharField(max_length=128, blank=True, null=True)
    queue_name = models.CharField(max_length=128)
    interface = models.CharField(max_length=128, blank=True, null=True)
    penalty = models.BigIntegerField(null=True, editable=False)
    paused = models.BigIntegerField(null=True, editable=False)


class SipPeers(models.Model):

    accountcode = models.CharField(max_length=128, blank=True, null=True)
    directmedia = models.CharField(max_length=128, null=True, editable=False)
    disallow = models.CharField(
        max_length=128, blank=True, null=True, default='all', editable=False)
    allow = models.CharField(max_length=128, blank=True,
                             null=True, default='alaw;ulaw;gsm;g729', editable=False)
    # allowoverlap = models.TextChoices(
    #     'yes', 'no', editable=False)
    # allowoverlap = models.CharField(
    #     max_length=10, choices=MyChoice.choices, editable=False, default='yes')

    # allowsubscribe = models.TextChoices(
    #     'yes', 'no', editable=False)
    allowtransfer = models.CharField(max_length=128, null=True, editable=False)
    amaflags = models.CharField(max_length=128, null=True, editable=False)
    autoframing = models.CharField(
        max_length=128, blank=True, null=True, editable=False)
    auth = models.CharField(max_length=128, null=True, editable=False)
    # buggymwi = models.TextChoices('yes', 'no', default='yes', editable=False)
    callgroup = models.CharField(max_length=128, null=True, editable=False)
    callerid = models.CharField(max_length=128, null=True, editable=False)
    cid_number = models.CharField(max_length=128, null=True, editable=False)
    fullname = models.CharField(max_length=128, null=True)
    # call-limit = models.IntegerField(blank=True, null=True, editable=False)
    callingpres = models.CharField(max_length=128, null=True, editable=False)
    # canreinvite = models.CharField(
    #     max_length=10, null=True, default='yes', editable=False)
    context = models.CharField(
        max_length=128, null=True, default='phones', editable=False)
    callbackextension = models.CharField(
        max_length=128, null=True, editable=False)
    defaultip = models.CharField(max_length=128, null=True, editable=False)
    defaultuser = models.CharField(max_length=128, null=True, editable=False)
    dtmfmode = models.CharField(max_length=128, null=True, editable=False)
    encryption = models.CharField(max_length=128, null=True, editable=False)
    fromuser = models.CharField(max_length=128, null=True, editable=False)
    fromdomain = models.CharField(max_length=128, null=True, editable=False)
    fullcontact = models.CharField(max_length=128, null=True,  editable=False)
    # g726nonstandard = models.TextChoices(
    #     'yes', 'no', default='no', editable=False)
    host = models.CharField(max_length=128, null=True,
                            editable=False, default='dynamic')
    insecure = models.CharField(max_length=128, null=True, editable=False)
    ipaddr = models.CharField(max_length=128, null=True, editable=False)
    language = models.CharField(max_length=10, null=True, editable=False)
    lastms = models.CharField(max_length=128, null=True, editable=False)
    mailbox = models.CharField(max_length=128, null=True, editable=False)
    maxcallbitrate = models.BigIntegerField(
        null=True, default=385, editable=False)
    mohsuggest = models.CharField(max_length=128, null=True, editable=False)
    md5secret = models.CharField(max_length=128, null=True, editable=False)
    musiconhold = models.CharField(max_length=128, null=True, editable=False)
    name = models.CharField(max_length=128)
    nat = models.CharField(max_length=128, null=True, editable=False)
    outboundproxy = models.CharField(max_length=128, null=True, editable=False)
    deny = models.CharField(max_length=128, null=True, editable=False)
    permit = models.CharField(max_length=128, null=True, editable=False)
    pickupgroup = models.CharField(max_length=128, null=True, editable=False)
    port = models.CharField(max_length=128, null=True, editable=False)
    # progressinband = models.TextChoices(
    #     'yes', 'no', editable=False)
    # promiscredir = models.TextChoices(
    # 'yes', 'no', editable=False)
    qualify = models.CharField(max_length=15, null=True, editable=False)
    regexten = models.CharField(max_length=128, null=True, editable=False)
    regseconds = models.IntegerField(blank=True, null=True, editable=False)
    # rfc2833compensate = models.TextChoices(
    # 'yes', 'no', editable=False)
    rtptimeout = models.CharField(max_length=15, null=True, editable=False)
    rtpholdtimeout = models.CharField(max_length=15, null=True, editable=False)
    secret = models.CharField(max_length=128, null=True)
    # sendrpid = models.TextChoices('yes', 'no', editable=False)
    setvar = models.CharField(max_length=128, null=True, editable=False)
    subscribecontext = models.CharField(
        max_length=128, null=True, editable=False)
    subscribemwi = models.CharField(max_length=128, null=True, editable=False)
    # t38pt_udptl = models.TextChoices('yes', 'no', default='no', editable=False)
    transport = models.CharField(max_length=128, null=True, editable=False)
    # trustrpid = models.TextChoices('yes', 'no', default='no', editable=False)
    type = models.CharField(max_length=128, null=True,
                            default='friend', editable=False)
    # useclientcode = models.TextChoices(
    #     'yes', 'no', default='no', editable=False)
    usereqphone = models.CharField(max_length=128, null=True, editable=False)
    username = models.CharField(max_length=128, null=True)
    # videosupport = models.TextChoices(
    #     'yes', 'no', default='yes', editable=False)
    vmexten = models.CharField(max_length=128, null=True, editable=False)
