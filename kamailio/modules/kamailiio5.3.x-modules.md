# Kamailio Modules - v5.3.x (stable)



| Module |	Description |	Status |
| :---: |	:---: |	:---: |
ACC |	Accounting module |	released
ACC_DIAMETER |	Accounting module for DIAMETER backend |	alpha
ACC_JSON |	Accounting module generating a JSON document pushed to MQueue |	released
ACC_RADIUS |	Accounting module for RADIUS backend |	released
ALIAS_DB |	Database aliases module |	released
APP_JAVA |	Execute embedded Java applications |	released
APP_JSDT |	Execute embedded JavaScript scripts |	released
APP_LUA |	Execute embedded Lua scripts |	released
APP_LUA_SR |	Export old Lua sr library |	new
APP_MONO |	Execute embedded managed code (e.g., C#, VisualBasic.NET, Java, Java Script) |	released
APP_PERL |	Embed execution of Perl functions |	released
APP_PYTHON |	Execute embedded Python2 scripts |	released
APP_PYTHON3 |	Execute embedded Python3 scripts |	released
APP_RUBY |	Execute embedded Ruby scripts |	released
APP_SQLANG |	Execute embedded Squirrel language scripts |	released
ASYNC |	Asynchronous SIP request handling functions |	released
AUTH |	Authentication Interface module |	released
AUTH_DB |	Database-backend authentication module |	released
AUTH_DIAMETER |	DIAMETER-backend authentication module |	alpha
AUTH_EPHEMERAL |	User authentication with ephemeral credentials |	released
AUTH_IDENTITY |	Identity authentication module |	released
AUTH_RADIUS |	RADIUS-backend authentication module |	released
AUTH_XKEYS |	Shared keys authentication module |	released
AVP |	Collection of functions for handling AVPs |	from-ser
AVPOPS |	AVP operations module |	released
BENCHMARK |	Config file benchmarking |	released
BLST |	Blacklisting API for config |	released
CALL_CONTROL |	Conector to call_control application |	released
CALL_OBJ |	Assign integer ids to calls from a ring pool of values |	released
CARRIERROUTE |	Routing extension suitable for carriers |	released
CDP |	C Diameter Peer - core communication engine |	released
CDP_AVP |	C Diameter Peer - application extensions |	released
CFG_DB |	Load core and module parameters from database |	released
CFG_RPC |	Update core and module parameters at runtime via RPC interface |	released
CFGUTILS |	Different config utilities |	released
CFGT |	Unit test config file execution tracing |	released
CNXCC |	Credit control module - prepaid system |	released
COREX |	Core extensions via module interface |	released
COUNTERS |	Internal counter API for config |	released
CPLC |	CPL interpreter module |	renamed
CRYPTO |	Cryptographic extensions for use in config |	released
CTL |	Control connector for RPC interface (fifo, unixsock, tcp, udp) |	released
DB_BERKELEY |	Berkeley DB driver for DB API |	released
DB_CASSANDRA |	Cassandra database server connector |	released
DB_CLUSTER |	Generic database connectors clustering |	released
DB_FLATSTORE |	Fast writting-only text-backend for database module |	released
DB_MONGODB |	MongoDB connector for DB APIv1 |	released
DB_MYSQL |	MYSQL-backend for database API module |	released
DB_ORACLE |	Oracle driver for DB API |	released
DB_PERLVDB |	Perl Virtual Database engine |	released
DB_POSTGRES |	POSTGRES-backend for database API module |	released
DB_REDIS |	Redis-backend for database API module |	released
DB_SQLITE |	SQLITE-backend for database API module |	released
DB_TEXT |	Text-backend for database API module |	released
DB_UNIXODBC |	unixODBC driver module |	released
DB2_LDAP |	DB APIv2 connector to LDAP servers |	from-ser
DB2_OPS |	DB APIv2 config operations |	from-ser
DEBUGGER |	Interactive config debugger |	released
DIALOG |	Dialog support module |	released
DIALPLAN |	Dialplan translation module |	released
DISPATCHER |	Dispatcher (load-balancer) module |	released
DIVERSION |	Diversion header insertion module |	released
DMQ |	Distributed Message Queue System using SIP |	released
DMQ_USRLOC |	User location replication using DMQ |	released
DNSSEC |	DNSSEC implementation for SIP routing |	released
DOMAIN |	Multi-domain support module	released |
DOMAINPOLICY |	Policies to connect federations |	released
DROUTING |	Yet another prefix routing module |	released
ENUM	ENUM lookup module |	released
ERLANG	Erlang node connector module |	released
EVAPI	Network event broadcast API	released
EVREXEC	Execut event routes at startup on dedicated processes	released
EXEC	External application execution module	released
GEOIP	GeoIP API to config file	released
GEOIP2	GeoIP API to config file using the new library with IPv6 support	released
GROUP	User-groups module with DB-backend	released
GZCOMPRESS	Compress and decompress SIP message body with zlib	released
H350	H350 implementation	released
HTABLE	Generic Hash Table container in shared memory	released
HTTP_CLIENT	Sync and async HTTP client using CURL library	released
HTTP_ASYNC_CLIENT	Alternative async HTTP client using CURL and event libraries	released
IMS_AUTH	IMS authentication module	released
IMS_CHARGING	IMS charging component module	released
IMS_DIALOG	IMS dialog tracking module	released
IMS_DIAMETER_SERVER	IMS DIAMETER server module	released
IMS_ICSCF	IMS ICSCF component module	released
IMS_IPSEC_PCSCF	IMS IPSEC PCSCF module	released
IMS_ISC	IMS ISC component module	released
IMS_OCS	IMS OCS component module	released
IMS_QOS	IMS Diameter Rx interface between PCSCF and PCRF functions	released
IMS_REGISTRAR_PCSCF	IMS PCSCF registrar module	released
IMS_REGISTRAR_SCSCF	IMS SCSCF registrar module	released
IMS_USRLOC_PCSCF	IMS PCSCF usrloc module	released
IMS_USRLOC_SCSCF	IMS SCSCF usrloc module	released
IMC	Instant Messaging Conferencing module	released
IPOPS	IP and DNS related operations for configuration file	released
JANSSON	JSON document management using jansson library	released
JANSSONRPCC	JSON-RPC client over netstrings using jansson library	renamed
JSON	JSON document management using json-c library	released
JSONRPCC	JSON-RPC client over netstrings using json-c library	renamed
JSONRPCS	JSON-RPC server over HTTP	renamed
KAZOO	Middle layer connector for Kazoo VoIP platform	released
KEEPALIVE	Manage SIP-based keepalive monitoring of remote peers	released
KEMIX	Kamailio KEMI specific extensions module	new
KEX	Kamailio core extensions module	released
LCR	Least Cost Routing module	released
LDAP	LDAP connector	released
LOG_CUSTOM	Logging to custom backends	released
LOG_SYSTEMD	Logging to systemd journal	released
LOST	HELD (RFC6155) and LOST (RFC5222) location-based routing	new
MALLOC_TEST	Functions for stress-testing memory manager	from-ser
MANGLER	SIP message mangling functions	from-ser
MATRIX	Matrix operations	released
MAXFWD	Max-Forward processor module	released
MEDIAPROXY	NAT traversal module using mediaproxy	released
MEMCACHED	Memcached connector module	released
MISC_RADIUS	Generic RADIUS functions, replaces avp_radius, uri_radius and group_radius	released
MOHQUEUE	Music on hold queuing system	released
MQUEUE	Message queue system for config file	released
MSILO	SIP message silo module	released
MSRP	Embedded MSRP relay (RFC4975 and RFC4976)	released
MTREE	Generic memory caching system using tree indexes	released
NATHELPER	NAT traversal module - signaling functions	released
NAT_TRAVERSAL	Alternative NAT traversal module	released
NDB_CASSANDRA	Config connector to CASSANDRA NoSQL database engine	released
NDB_MONGODB	Config connector to MongoDB NoSQL database engine	released
NDB_REDIS	Config connector to REDIS NoSQL database engine	released
NOSIP	Handle non-sip messages received by SIP workers via event_route	released
NSQ	NSQ consumer for configuration file	released
OSP	OSP peering module	released
OUTBOUND	SIP Outbound implementation	released
P_USRLOC	Partitioned and distributed user location services	released
PATH	Path support for SIP loadbalancer	released
PDB	Number portability module	released
PDT	Prefix-to-Domain translator module	released
PEERING	RADIUS peering module	released
PERMISSIONS	Permissions control module	released
PHONENUM	Phone number lookup and normalization using libphonenumber	released
PIKE	Flood detector module	released
PIPELIMIT	Traffic shaping policies	released
PREFIX_ROUTE	Execute config file route blocks based on prefix	released
PRESENCE	Presence server module - common API	released
PRESENCE_CONFERENCE	Extension to Presence server for conference events handling	released
PRESENCE_DIALOGINFO	Extension to Presence server for Dialog Info	released
PRESENCE_MWI	Extension to Presence server for Message Waiting Indication	released
PRESENCE_PROFILE	Presence server module - user profile extensions - RFC6080	released
PRESENCE_XML	Presence server module - presence & watcher info and XCAP	released
PRESENCE_REGINFO	Extension to Presence server for registration info replication (RFC3680)	released
PRINT	Basic sample of a module (devel)	from-ser
PRINT_LIB	Basic sample of a module with internal lib dependency (devel)	from-ser
PUA	Common API for presence user agent client	released
PUA_BLA	BLA extension for PUA	released
PUA_DIALOGINFO	Dialog Info extension for PUA	released
PUA_JSON	PUA extensions using JSON documents	released
PUA_REGINFO	Extension to PUA server for registration info replication (RFC3680)	released
PUA_RPC	RPC extensions for PUA	released
PUA_USRLOC	USRLOC extension for PUA	released
PUA_XMPP	XMPP extension for PUA (SIMPLE-XMPP presence gateway)	released
PURPLE	Multi-protocol gateway using Purple library	released
PV	Module holding Pseudo-Variables	released
QOS	QOS control API	released
RABBITMQ	RabbitMQ client for configuration file	released
RATELIMIT	Traffic shaping module	released
REGEX	Regular expression matching using PCRE	released
REGISTRAR	SIP Registrar implementation module	released
RLS	Resource List Server implementation	released
RR	Record-Route and Route module	released
RTIMER	Execute config route blocks on timer basis	released
RTJSON	SIP routing based on JSON API	released
RTP_MEDIA_SERVER	RTP media server implementation	new
RTPENGINE	RTPEngine media relay control functions	released
RTPPROXY	RTPProxy media relay control functions	released
SANITY	SIP message formatting sanity checks	released
SCA	Shared Call Appearances	released
SCTP	SCTP Transport Layer	released
SDPOPS	SDP operations	released
SEAS	Sip Express Application Server (interface module)	released
SECFILTER	SIP securty filtering rules	new
SIPCAPTURE	SIP capture server module, used in Homer project	released
SIPDUMP	Save SIP traffic and associated runtime attributes	released
SIPT	SIP-T and SIP-I operations	released
SIPTRACE	SIP traffic tracing module	released
SIPUTILS	SIP utilities	released
SL	Stateless replier module	released
SMS	SIP-to-SMS IM gateway module	released
SMSOPS	Tools for handling SMS packets in SIP messages	released
SNMPStats	SNMP interface for statistics module	released
SPEEDDIAL	Per-user speed-dial controller module	released
SQLOPS	SQL operations	released
SS7OPS	JSON Operations for SS7 over HEP	released
SST	SIP Session Timer support	released
STATISTICS	Script statistics support	released
STATSC	Statistics collector providing reports	released
STATSD	Connector for statsd application	released
STUN	STUN requirements for SIP outbound	released
TCPOPS	Options to tune TCP connections at runtime	released
TEXTOPS	Text operations module	released
TEXTOPSX	Extra text operations	released
TIMER	Execute routing blocks on core timers	from-ser
TLS	TLS operations module	released
TM	Transaction (stateful) module	released
TMREC	Match time recurrences defined based on RFC2445	released
TMX	Transaction management extenstions module	released
TOPOH	Topology hiding module	released
TOPOS	Topology stripping module	released
TOPOS_REDIS	Redis backend for topos module	released
TSILO	Transaction storage container for dynamic new branches	released
UAC	UAC functionalies (FROM mangling and UAC auth)	released
UAC_REDIRECT	UAC redirection functionality	released
UID_AUTH_DB	Authentication module using unique ids	from-ser
UID_AVP_DB	AVP database operations using unique ids	from-ser
UID_DOMAIN	Domains management using unique ids	from-ser
UID_GFLAGS	Global attributes and flags using unique ids	from-ser
UID_URI_DB	Database URI operations using unique ids	from-ser
URI_DB	URI operations with database support module	released
USERBLACKLIST	User specific blacklists	released
USRLOC	User location implementation module	released
UTILS	A set of useful functions	released
UUID	Unique string value generator using libuuid	released
WEBSOCKET	WebSocket transport layer	released
XCAP_CLIENT	XCAP client implementation	released
XCAP_SERVER	XCAP server implementation	released
XHTTP	Basic HTTP request handling server	released
XHTTP_PI	Embedded provisioning interface over HTTP	released
XHTTP_PROM	XHTTP Promotheus metrics	new
XHTTP_RPC	RPC commands handling over HTTP	released
XLOG	Advanced logger module	released
XMLOPS	XML operations in config file using XPATH	released
XMLRPC	XMLRPC connector for RPC interface	released
XMPP	SIP-to-XMPP Gateway (SIP to Jabber/Google Talk)	released
XPRINT	Functions for printing messages with specifiers	from-ser
