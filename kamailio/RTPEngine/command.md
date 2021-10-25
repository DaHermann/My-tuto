The *ng* Control Protocol
=========================

In order to enable several advanced features in *rtpengine*, a new advanced control protocol has been devised
which passes the complete SDP body from the SIP proxy to the *rtpengine* daemon, has the body rewritten in
the daemon, and then passed back to the SIP proxy to embed into the SIP message.

This control protocol is based on the [bencode](http://en.wikipedia.org/wiki/Bencode) standard and runs over
UDP transport. *Bencoding* supports a similar feature set as the more popular JSON encoding (dictionaries/hashes,
lists/arrays, arbitrary byte strings) but offers some benefits over JSON encoding, e.g. simpler and more efficient
encoding, less encoding overhead, deterministic encoding and faster encoding and decoding. A disadvantage over
JSON is that it's not a readily human readable format.

Each message passed between the SIP proxy and the media proxy contains of two parts: a message cookie, and a
bencoded dictionary, separated by a single space. The message cookie serves the same purpose as in the control
protocol used by *Kamailio*'s *rtpproxy* module: matching requests to responses, and retransmission detection.
The message cookie in the response generated to a particular request therefore must be the same as in the
request.

The dictionary of each request must contain at least one key called `command`. The corresponding value must be
a string and determines the type of message. Currently the following commands are defined:

* ping
* offer
* answer
* delete
* query
* start recording
* stop recording
* block DTMF
* unblock DTMF
* block media
* unblock media
* silence media
* unsilence media
* start forwarding
* stop forwarding
* play media
* stop media
* play DTMF
* statistics
* publish
* subscribe request
* subscribe answer
* unsubscribe

The response dictionary must contain at least one key called `result`. The value can be either `ok` or `error`.
For the `ping` command, the additional value `pong` is allowed. If the result is `error`, then another key
`error-reason` must be given, containing a string with a human-readable error message. No other keys should
be present in the error case. If the result is `ok`, the optional key `warning` may be present, containing a
human-readable warning message. This can be used for non-fatal errors.

For readability, all data objects below are represented in a JSON-like notation and without the message cookie.
For example, a `ping` message and its corresponding `pong` reply would be written as:

	{ "command": "ping" }
	{ "result": "pong" }

While the actual messages as encoded on the wire, including the message cookie, might look like this:

	5323_1 d7:command4:pinge
	5323_1 d6:result4:ponge

All keys and values are case-sensitive unless specified otherwise. The requirement stipulated by the *bencode*
standard that dictionary keys must be present in lexicographical order is not currently honoured.

The *ng* protocol is used by *Kamailio*'s *rtpengine* module, which is based on the older module called *rtpproxy-ng*.

`ping` Message
--------------

The request dictionary contains no other keys and the reply dictionary also contains no other keys. The
only valid value for `result` is `pong`.

`offer` Message
---------------

The request dictionary must contain at least the following keys:

* `sdp`

  Contains the complete SDP body as string.

* `call-id`

  The SIP call ID as string.

* `from-tag`

  The SIP `From` tag as string.

Optionally included keys are:

* `via-branch`

	The SIP `Via` branch as string. Used to additionally refine the matching logic between media streams
	and calls and call branches.

* `label` or `from-label`

	A custom free-form string which *rtpengine* remembers for this participating endpoint and reports
	back in logs and statistics output. For some commands (e.g. `block media`) the given label is not
	used to set the label of the call participant, but rather to select an existing call participant.

* `set-label` or `to-label`

	Some commands (e.g. `block media`) use the given `label` to select
	an existing call participant. For these commands, `set-label` instead
	of `label` can be used to set the label at the same time, either for
	the selected call participant (if selected via `from-tag`) or for the
	newly created participant (e.g. for `subscribe request`).

* `flags`

	The value of the `flags` key is a list. The list contains zero or more of the following strings.
	Spaces in each string my be replaced by hyphens.

	- `SIP source address`

		Ignore any IP addresses given in the SDP body and use the source address of the received
		SIP message (given in `received from`) as default endpoint address. This was the default
		behaviour of older versions of *rtpengine* and can still be made the default behaviour
		through the `--sip-source` CLI switch.
		Can be overridden through the `media address` key.

	- `trust address`

		The opposite of `SIP source address`. This is the default behaviour unless the CLI switch
		`--sip-source` is active. Corresponds to the *rtpproxy* `r` flag.
		Can be overridden through the `media address` key.

	- `symmetric`

		Corresponds to the *rtpproxy* `w` flag. Not used by *rtpengine* as this is the default,
		unless `asymmetric` is specified.

	- `asymmetric`

		Corresponds to the *rtpproxy* `a` flag. Advertises an RTP endpoint which uses asymmetric
		RTP, which disables learning of endpoint addresses (see below).

	- `unidirectional`

		When this flag is present, kernelize also one-way rtp media.

	- `strict source`

		Normally, *rtpengine* attempts to learn the correct endpoint address for every stream during
		the first few seconds after signalling by observing the source address and port of incoming
		packets (unless `asymmetric` is specified). Afterwards, source address and port of incoming
		packets are normally ignored and packets are forwarded regardless of where they're coming from.
		With the `strict source` option set, *rtpengine* will continue to inspect the source address
		and port of incoming packets after the learning phase and compare them with the endpoint
		address that has been learned before. If there's a mismatch, the packet will be dropped and
		not forwarded.

	- `media handover`

		Similar to the `strict source` option, but instead of dropping packets when the source address
		or port don't match, the endpoint address will be re-learned and moved to the new address. This
		allows endpoint addresses to change on the fly without going through signalling again. Note that
		this opens a security hole and potentially allows RTP streams to be hijacked, either partly or
		in whole.

	- `reset`

		This causes *rtpengine* to un-learn certain aspects of the RTP endpoints involved, such as
		support for ICE or support for SRTP. For example, if `ICE=force` is given, then *rtpengine*
		will initially offer ICE to the remote endpoint. However, if a subsequent answer from that
		same endpoint indicates that it doesn't support ICE, then no more ICE offers will be made
		towards that endpoint, even if `ICE=force` is still specified. With the `reset` flag given,
		this aspect will be un-learned and *rtpengine* will again offer ICE to this endpoint.
		This flag is valid only in an `offer` message and is useful when the call has been
		transferred to a new endpoint without change of `From` or `To` tags.

	- `port latching`

		Forces *rtpengine* to retain its local ports during a signalling exchange even when the
		remote endpoint changes its port.

	- `no port latching`

		Port latching is enabled by default for endpoints which speak
		ICE. With this option preset, a remote port change will result
		in a local port change even for endpoints which speak ICE,
		which will imply an ICE restart.

	- `record call`

		Identical to setting `record call` to `on` (see below).

	- `no rtcp attribute`

		Omit the `a=rtcp` line from the outgoing SDP.

	- `full rtcp attribute`

		Include the full version of the `a=rtcp` line (complete with network address) instead of
		the short version with just the port number.

	- `loop protect`

		Inserts a custom attribute (`a=rtpengine:...`) into the outgoing SDP to prevent *rtpengine*
		processing and rewriting the same SDP multiple times. This is useful if your setup
		involves signalling loops and need to make sure that *rtpengine* doesn't start looping
		media packets back to itself. When this flag is present and *rtpengine* sees a matching
		attribute already present in the SDP, it will leave the SDP untouched and not process
		the message.

	- `always transcode`

		Legacy flag, synonymous to `codec-accept=all`.

	- `single codec`

		Using this flag in an `answer` message will leave only the first listed codec in place
		and will remove all others from the list. Useful for RTP clients which get confused if
		more than one codec is listed in an answer.

	- `reuse codecs` or `no codec renegotiation`

		Instructs *rtpengine* to prevent endpoints from switching codecs during call run-time
		if possible. Codecs that were listed as preferred in the past will be kept as preferred
		even if the re-offer lists other codecs as preferred, or in a different order. Recommended
		to be combined with `single codec`.

	- `allow transcoding`

		This flag is only useful in commands that provide an explicit answer SDP to *rtpengine*
		(e.g. `subscribe answer`). For these commands, if the answer SDP does not accept all
		codecs that were offered, the default behaviour is to reject the answer. With this flag
		given, the answer will be accepted even if some codecs were rejected, and codecs will be
		transcoded as required.

	- `all`

		Only relevant to the `unblock media` and `unsilence media`
		messages. Instructs *rtpengine* to remove not only a full-call
		media block, but also remove directional media blocks that were
		imposed on individual participants.

	- `pad crypto`

		Legacy alias to SDES=pad.


	- `generate mid`

		Add `a=mid` attributes to the outgoing SDP if they were not already present.

	- `strip extmap`

		Remove `a=rtpmap` attributes from the outgoing SDP.

	- `original sendrecv`

		With this flag present, *rtpengine* will leave the media direction attributes
		(`sendrecv`, `recvonly`, `sendonly`, and `inactive`) from the received SDP body
		unchanged. Normally *rtpengine* would consume these attributes and insert its
		own version of them based on other media parameters (e.g. a media section with
		a zero IP address would come out as `sendonly` or `inactive`).

	- `inject DTMF`

		Signals to *rtpengine* that the audio streams involved in this `offer` or `answer`
		(the flag should be present in both of them) are to be made available for DTMF
		injection via the `play DTMF` control message. See `play DTMF` below for additional
		information.

	- `generate RTCP`

		Identical to setting `generate RTCP = on`.

	- `debug` or `debugging`

		Enabled full debug logging for this call, regardless of global log level settings.

	- `pierce NAT`

		Sends empty UDP packets to the remote RTP peer as soon as an
		endpoint address is available from a received SDP, for as long
		as no incoming packets have been received. Useful to create an
		initial NAT mapping. Not needed when ICE is in use.

	- `NAT-wait`

		Prevents forwarding media packets to the respective endpoint
		until at least one media packet has been received from that
		endpoint. This is to allow a NAT binding to open in the ingress
		direction before sending packets out, which could result in an
		automated firewall block.

	- `trickle ICE`

		Useful for `offer` messages when ICE as advertised to also advertise
		support for trickle ICE.

* `generate RTCP`

	Contains a string, either `on` or `off`. If enabled for a call,
	received RTCP packets will not simply be passed through as usual, but
	instead will be consumed, and instead *rtpengine* will generate its own
	RTCP packets to send to the RTP peers. This flag will be effective for
	both sides of a call.

* `replace`

	Similar to the `flags` list. Controls which parts of the SDP body should be rewritten.
	Contains zero or more of:

	- `origin`

		Replace the address found in the *origin* (o=) line of the SDP body. Corresponds
		to *rtpproxy* `o` flag.

	- `session connection` or `session-connection`

		Replace the address found in the *session-level connection* (c=) line of the SDP body.
		Corresponds to *rtpproxy* `c` flag.

	- `SDP version` or `SDP-version`

		Take control of the version field in the SDP and make sure it's increased every
		time the SDP changes, and left unchanged if the SDP is the same.

	- `username`

		Take control of the origin username field in the SDP. With this
		option in use, *rtpengine* will make sure the username field in
		the `o=` line always remains the same in all SDPs going to a
		particular RTP endpoint.

	- `session name` or `session-name`

		Same as `username` but for the entire contents of the `s=` line.

	- `zero address`

		Using a zero endpoint address is an obsolete way to signal a
		muted or sendonly stream. Streams with zero addresses are
		normally flagged as sendonly and the zero address in the SDP is
		passed through. With this option set, the zero address is
		replaced with a real address.

* `direction`

	Contains a list of two strings and corresponds to the *rtpproxy* `e` and `i` flags. Each element must
	correspond to one of the named logical interfaces configured on the
	command line (through `--interface`). For example, if there is one logical interface named `pub` and
	another one named `priv`, then if side A (originator of the message) is considered to be
	on the private network and side B (destination of the message) on the public network, then that would
	be rendered within the dictionary as:

		{ ..., "direction": [ "priv", "pub" ], ... }

	This only needs to be done for an initial `offer`; for the `answer` and any subsequent offers (between
	the same endpoints) *rtpengine* will remember the selected network interface.

	As a special case to support legacy usage of this option, if the given interface names are
	`internal` or `external` and if no such interfaces have been configured, then they're understood as
	selectors between IPv4 and IPv6 addresses.
	However, this mechanism for selecting the address family is now obsolete
	and the `address family` dictionary key should be used instead.

	For legacy support, the special direction keyword `round-robin-calls` can be used to invoke the
	round-robin interface selection algorithm described in the section *Interfaces configuration*.
	If this special keyword is used, the round-robin selection will run over all configured
	interfaces, whether or not they are configured using the `BASE:SUFFIX` interface name notation.
	This special keyword is provided only for legacy support and should be considered obsolete.
	It will be removed in future versions.

* `interface`

	Contains a single string naming one of the configured interfaces, just like `direction` does. The
	`interface` option is used instead of `direction` where only one interface is required (e.g. outside
	of an offer/answer scenario), for example in the `publish` or `subscribe request` commands.

* `received from`

	Contains a list of exactly two elements. The first element denotes the address family and the second
	element is the SIP message's source address itself. The address family can be one of `IP4` or `IP6`.
	Used if SDP addresses are neither trusted (through `SIP source address` or `--sip-source`) nor the
	`media address` key is present.

* `drop-traffic`

	Contains a string, valid values are `start` or `stop`.

	`start` signals to *rtpengine* that all RTP involved in this call is dropped.
	Can be present either in `offer` or `answer`, the behavior is for the entire call.

	`stop` signals to *rtpengine* that all RTP involved in this call is NOT dropped anymore.
	Can be present either in `offer` or `answer`, the behavior is for the entire call.

	`stop` has priority over `start`, if both are present.

* `ICE`

	Contains a string which must be one of the following values:

	With `remove`, any ICE attributes are stripped from the SDP body.

	With `force`, ICE attributes are first stripped, then new attributes are
	generated and inserted, which leaves the media proxy as the only ICE candidate.

	With `default`, the behaviour will be the same as with `force` if the incoming SDP already
	had ICE attributes listed. If the incoming SDP did not contain ICE attributes, then no
	ICE attributes are added.

	With `force-relay`, existing ICE candidates are left in place except `relay`
	type candidates, and *rtpengine* inserts itself as a `relay` candidate. It will also leave SDP
	c= and m= lines unchanged.

	With `optional`, if no ICE attributes are present, a new set is generated and the
	media proxy lists itself as ICE candidate; otherwise, the media proxy inserts itself as a
	low-priority candidate. This used to be the default behaviour in previous versions of
	*rtpengine*.

	The default behaviour (no `ICE` key present at all) is the same as `default`.

	This flag operates independently of the `replace` flags.

	Note that if config parameter `save-interface-ports = true`, ICE will be broken, because
	rtpengine will bind ports only on the first local interface of desired family of logical interface.

* `ICE-lite`

	Contains a string which must be one of the following values:

	- `forward` to enable "ICE lite" mode towards the peer that this offer is sent to.

	- `backward` to enable "ICE lite" mode towards the peer that has sent this offer.

	- `both` to enable "ICE lite" towards both peers.

	- `off` to disable "ICE lite" towards both peers and revert to full ICE support.

	The default (keyword not present at all) is to use full ICE support, or to leave the previously
	set "ICE lite" mode unchanged. This keyword is valid in `offer` messages only.

* `transport protocol`

	The transport protocol specified in the SDP body is to be rewritten to the string value given here.
	The media
	proxy will expect to receive this protocol on the allocated ports, and will talk this protocol when
	sending packets out. Translation between different transport protocols will happen as necessary.

	Valid values are: `RTP/AVP`, `RTP/AVPF`, `RTP/SAVP`, `RTP/SAVPF`.

	Additionally the string `accept` can be given in `answer` messages to allow a special case: By
	default (when no `transport-protocol` override is given) in answer messages, *rtpengine* will
	use the transport protocol that was originally offered. However, an answering client may answer
	with a different protocol than what was offered (e.g. offer was for `RTP/AVP` and answer comes
	with `RTP/AVPF`). The default behaviour for *rtpengine* is to ignore this protocol change and
	still proceed with the protocol that was originally offered. Using the `accept` option here
	tells *rtpengine* to go along with this protocol change and pass it to the original offerer.

* `media address`

	This can be used to override both the addresses present in the SDP body
	and the `received from` address. Contains either an IPv4 or an IPv6 address, expressed as a simple
	string. The format must be dotted-quad notation for IPv4 or RFC 5952 notation for IPv6.
	It's up to the RTP proxy to determine the address family type.

* `address family`

	A string value of either `IP4` or `IP6` to select the primary address family in the substituted SDP
	body. The default is to auto-detect the address family if possible (if the receiving end is known
	already) or otherwise to leave it unchanged.

* `rtcp-mux`

	A list of strings controlling the behaviour regarding rtcp-mux (multiplexing RTP and RTCP on a single
	port, RFC 5761). The default behaviour is to go along with the client's preference. The list can contain
	zero of more of the following strings. Note that some of them are mutually exclusive.

	- `offer`

		Instructs *rtpengine* to always offer rtcp-mux, even if the client itself doesn't offer it.

	- `require`

		Similar to `offer` but pretends that the receiving client has already accepted rtcp-mux.
		The effect is that no separate RTCP ports will be advertised, even in an initial offer
		(which is against RFC 5761). This option is provided to talk to WebRTC clients.

	- `demux`

		If the client is offering rtcp-mux, don't offer it to the other side, but accept it back to
		the offering client.

	- `accept`

		Instructs *rtpengine* to accept rtcp-mux and also offer it to the other side if it has been
		offered.

	- `reject`

		Reject rtcp-mux if it has been offered. Can be used together with `offer` to achieve the opposite
		effect of `demux`.

* `TOS`

	Contains an integer. If present, changes the TOS value for the entire call, i.e. the TOS value used
	in outgoing RTP packets of all RTP streams in all directions. If a negative value is used, the previously
	used TOS value is left unchanged. If this key is not present or its value is too large (256 or more), then
	the TOS value is reverted to the default (as per `--tos` command line).

* `DTLS`

	Contains a string and influences the behaviour of DTLS-SRTP. Possible values are:

	- `off` or `no` or `disable`

		Prevents *rtpengine* from offering or acceping DTLS-SRTP when otherwise it would. The default
		is to offer DTLS-SRTP when encryption is desired and to favour it over SDES when accepting
		an offer.

	- `passive`

		Instructs *rtpengine* to prefer the passive (i.e. server) role for the DTLS
		handshake. The default is to take the active (client) role if possible. This is useful in cases
		where the SRTP endpoint isn't able to receive or process the DTLS handshake packets, for example
		when it's behind NAT or needs to finish ICE processing first.

	- `active`

		Reverts the `passive` setting. Only useful if the `dtls-passive` config option is set.

* `DTLS-reverse`

	Contains a string and influences the behaviour of DTLS-SRTP. Unlike the regular `DTLS` flag, this one
	is used to control behaviour towards DTLS that was offered to *rtpengine*. In particular, if `passive`
	mode is used, it prevents *rtpengine* from prematurely sending active DTLS connection attempts.
	Possible values are:

	- `passive`

		Instructs *rtpengine* to prefer the passive (i.e. server) role for the DTLS
		handshake. The default is to take the active (client) role if possible. This is useful in cases
		where the SRTP endpoint isn't able to receive or process the DTLS handshake packets, for example
		when it's behind NAT or needs to finish ICE processing first.

	- `active`

		Reverts the `passive` setting. Only useful if the `dtls-passive` config option is set.

* `DTLS-fingerprint`

	Contains a string and is used to select the hashing function to generate the DTLS fingerprint
	from the certificate. The default is SHA-256, or the same hashing function as was used by the
	peer. Available are `SHA-1`, `SHA-224`, `SHA-256`, `SHA-384`, and `SHA-512`.

* `SDES`

	A list of strings controlling the behaviour regarding SDES. The default is to offer SDES without any
	session parameters when encryption is desired, and to accept it when DTLS-SRTP is unavailable. If two
	SDES endpoints are connected to each other, then the default is to offer SDES with the same options
	as were received from the other endpoint. Additionally, all other supported SDES crypto suites are
	added to the outgoing offer by default.

	These options can also be put into the `flags` list using a prefix of `SDES-`. All options controlling
	SDES session parameters can be used either in all lower case or in all upper case.

	- `off` or `no` or `disable`

		Prevents *rtpengine* from offering SDES, leaving DTLS-SRTP as the other option.

	- `unencrypted_srtp`, `unencrypted_srtcp` and `unauthenticated_srtp`

		Enables the respective SDES session parameter (see section 6.3 or RFC 4568). The default is to
		copy these options from the offering client, or not to have them enabled if SDES wasn't offered.

	- `encrypted_srtp`, `encrypted_srtcp` and `authenticated_srtp`

		Negates the respective option. This is useful if one of the session parameters was offered by
		an SDES endpoint, but it should not be offered on the far side if this endpoint also speaks SDES.

	- `no-`*SUITE*

		Exclude individual crypto suites from being included in the offer. For example,
		`no-NULL_HMAC_SHA1_32` would exclude the crypto suite `NULL_HMAC_SHA1_32` from
		the offer. This has two effects: if a given crypto suite was present in a received
		offer, it will be removed and will be missing in the outgoing offer; and if a given crypto
		suite was not present in the received offer, it will not be added to it.

	- `pad`

		RFC 4568 (section 6.1) is somewhat ambiguous regarding the base64 encoding format of
		`a=crypto` parameters added to an SDP body. The default interpretation is that trailing
		`=` characters used for padding should be omitted. With this flag set, these padding
		characters will be left in place.

	- `lifetime`

		Add the key lifetime parameter `2^31` to each crypto key.

	- `static`

		Instructs *rtpengine* to skip the full SDES negotiation routine during a re-invite
		(e.g. pick the first support crypto suite, look for possible SRTP passthrough)
		and instead leave the previously negotiated crypto suite in place. Only useful in
		subsequent `answer` messages and ignored in `offer` messages.

* `OSRTP`

	Similar to `SDES` but controls OSRTP behaviour. Default behaviour is to pass through
	OSRTP negotiations. Supported options:

	- `offer`

		When processing a non-OSRTP offer, convert it to an OSRTP offer. Will result
		in RTP/SRTP transcoding if the OSRTP offer is accepted.

	- `accept`

		When processing a non-OSRTP answer in response to an OSRTP offer, accept the
		OSRTP offer anyway. Results in RTP/SRTP transcoding.

* `record call`

	Contains one of the strings `yes`, `no`, `on` or `off`. This tells the rtpengine
	whether or not to record the call to PCAP files. If the call is recorded, it
	will generate PCAP files for each stream and a metadata file for each call.
	Note that rtpengine *will not* force itself into the media path, and other
	flags like `ICE=force` may be necessary to ensure the call is recorded.

	See the `--recording-dir` option above.

	Enabling call recording via this option has the same effect as doing it separately
	via the `start recording` message, except that this option guarantees that the
	entirety of the call gets recorded, including all details such as SDP bodies
	passing through *rtpengine*.

* `metadata`

	This is a generic metadata string. The metadata will be written to the bottom of
	metadata files within `/path/to/recording_dir/metadata/` or to
	`recording_metakeys` table.  In the latter case, `metadata` string must
	contain a list of `key:val` pairs separated by `|` character.  `metadata` can be used to
	record additional information about recorded calls. `metadata` values passed in
	through subsequent messages will overwrite previous metadata values.

	See the `--recording-dir` option above.

* `codec`

	Contains a dictionary controlling various aspects of codecs (or RTP payload types).

	These options can also be put into the `flags` list using a prefix of `codec-`. For example,
	to set the codec options for two variants of Opus when they're implicitly accepted, (see
	the example under `set`), one would put the following into the `flags` list:
	`codec-set-opus/48000/1/16000` `codec-set-opus/48000/2/32000`

	The following keys are understood:

	* `strip`

		Contains a list of strings. Each string is the name of a codec or RTP payload
		type that should be removed from the SDP. Codec names are case sensitive, and
		can be either from the list of codecs explicitly defined by the SDP through
		an `a=rtpmap` attribute, or can be from the list of RFC-defined codecs. Examples
		are `PCMU`, `opus`, or `telephone-event`. Codecs stripped using this option
		are treated as if they had never been in the SDP.

		It is possible to specify codec format parameters alongside with the codec name
		in the same format as they're written in SDP for codecs that support them,
		for example `opus/48000` to
		specify Opus with 48 kHz sampling rate and one channel (mono), or
		`opus/48000/2` for stereo Opus. If any format parameters are specified,
		the codec will only be stripped if all of the format parameters match, and other
		instances of the same codec with different format parameters will be left
		untouched.

		As a special keyword, `all` can be used to remove all codecs, except the ones
		that should explicitly offered (see below). Note that it is an error to strip
		all codecs and leave none that could be offered. In this case, the original
		list of codecs will be left unchanged.

		The keyword `full` can also be used, which behaves the same as `all` with the
		exception listed under `transcode` below.

	* `except`

		Contains a list of strings. Each string is the name of a codec that should be
		included in the list of codecs offered. This is primarily useful to block all
		codecs (`strip -> all` or `mask -> all`) except the ones given in the `except`
		whitelist.  Codecs that were not present in the original list of codecs
		offered by the client will be ignored.

		This list also supports codec format parameters as per above.

	* `offer`

		This is identical to `except` but additionally allows the codec order to be
		changed. So the first codec listed in `offer` will be the primary (preferred)
		codec in the output SDP, even if it wasn't originally so.

	* `transcode`

		Similar to `offer` but allows codecs to be added to the list of offered codecs
		even if they were not present in the original list of codecs. In this case,
		the transcoding engine will be engaged. Only codecs that are supported for both
		decoding and encoding can be added in this manner. This also has the side effect
		of automatically stripping all unsupported codecs from the list of offered codecs,
		as *rtpengine* must expect to receive or even send in any codec that is present
		in the list.

		Note that using this option does not necessarily always engage the transcoding
		engine. If all codecs given in the `transcode` list were present in the original
		list of offered codecs, then no transcoding will be done. Also note that if
		transcoding takes place, in-kernel forwarding is disabled for this media stream
		and all processing happens in userspace.

		If no codec format parameters are specified in this list (e.g. just `opus`
		instead of `opus/48000/2`), default values will be chosen for them.

		For codecs that support different bitrates, it can be specified by appending
		another slash followed by the bitrate in bits per second,
		e.g. `opus/48000/2/32000`. In this case, all format parameters (clock rate,
		channels) must also be specified.

		Additional options that can be appended to the codec string with additional slashes
		are ptime, the `fmtp` string, and additional codec-specific options, for example
		`iLBC/8000/1///mode=30` to use as `fmtp`.

		If a literal `=` cannot be used due to parsing constraints (i.e. being wrongly
		interpreted as a key-value pair), it can be escaped by using two dashes instead,
		e.g. `iLBC/8000/1///mode--30`.

		As a special case, if the `strip=all` or `mask=all` option has been used and
		the `transcode` option is used on a codec that was originally present in the offer,
		then *rtpengine* will treat this codec the same as if it had been used with the
		`offer` option, i.e. it will simply restore it from the list of stripped codecs and
		won't actually engage transcoding for this codec. On the other hand, if a codec has
		been stripped explicitly by name using the `strip` or `mask` option and then used again
		with the `transcode` option, then the codec will not simply be restored from the
		list of stripped codecs, but instead a new transcoded instance of the codec will
		be inserted into the offer. (This special exception does not apply to `mask=full`
		or `strip=full`.)

		This option is only processed in `offer` messages and ignored otherwise.

	* `mask`

		Similar to `strip` except that codecs listed here will still be accepted and
		used for transcoding on the offering side. Useful only in combination with
		`transcode`. For example, if an offer advertises Opus and the options
		`mask=opus, transcode=G723` are given, then the rewritten outgoing offer
		will contain only G.723 as offered codec, and transcoding will happen
		between Opus and G.723. In contrast, if only `transcode=G723` were given, then
		the rewritten outgoing offer would contain both Opus and G.723. On the other
		hand, if `strip=opus, transcode=G723` were given, then Opus would be unavailable
		for transcoding.

		As with the `strip` option, the special keywords `all`  and `full` can be used
		to mask all codecs that have been offered.

		This option is only processed in `offer` messages and ignored otherwise.

	* `consume`

		Identical to `mask` but enables the transcoding engine even if no other transcoding
		related options are given.

	* `accept`

		Similar to `mask` and `consume` but doesn't remove the codec from the list of
		offered codecs. This means that a codec listed under `accept` will still be offered
		to the remote peer, but if the remote peer rejects it, it will still be accepted
		torwards the original offerer and then used for transcoding. It is a more selective
		version of what the `always transcode` flag does.

	* `set`

		Contains a list of strings. This list makes it possible to set codec options
		(bitrate in particular) for codecs that are implicitly accepted for transcoding.
		For example, if `AMR` was offered, `transcode=PCMU` was given, and the remote
		ended up accepting `PCMU`, then this option can be used to set the bitrate used
		for the AMR transcoding process.

		Each string must be a full codec specification as per above, including clock rate
		and number of channels. Using the example above, `set=AMR/8000/1/7400` can be used
		to transcode to AMR with 7.4 kbit/s.

		Codec options (bitrate) are only applied to codecs that match the given parameters
		(clock rate, channels), and multiple options can be given for the same coded with
		different parameters. For example, to specify different bitrates for Opus for both
		mono and stereo output, one could use `set=[opus/48000/1/16000,opus/48000/2/32000]`.

		This option is only processed in `offer` messages and ignored otherwise.

* `ptime`

	Contains an integer. If set, changes the `a=ptime` attribute's value in the outgoing
	SDP to the provided value. It also engages the transcoding engine for supported codecs
	to provide repacketization functionality, even if no additional codec has actually
	been requested for transcoding. Note that not all codecs support all packetization
	intervals.

	The selected ptime (which represents the duration of a single media packet in milliseconds)
	will be used towards the endpoint receiving this offer, even if the matching answer
	prefers a different ptime.

	This option is ignored in `answer` messages. See below for the reverse.

* `ptime-reverse`

	This is the reciprocal to `ptime`. It sets the ptime to be used towards the endpoint
	who has sent the offer. It will be inserted in the `answer` SDP. This option is also
	ignored in `answer` messages.

* `T.38`

	Contains a list of strings. Each string is a flag that controls the behaviour regarding
	T.38 transcoding. These flags are ignored if the message is not an `offer`.
	Recognised flags are:

	- `decode`

		If the received SDP contains a media section with an `image` type, `UDPTL`
		transport, and `t38` format string, this flag instructs *rtpengine* to convert
		this media section into an `audio` type using RTP as transport protocol.
		Other transport protocols (such as SRTP) can be selected using `transport protocol`
		as described above.

		The default audio codecs to be offered are `PCMU` and `PCMA`. Other audio codecs
		can be specified using the `transcode=` flag described above, in which case the
		default codecs will not be offered automatically.

	- `force`

		If the received SDP contains an audio media section using RTP transport, this flag
		instructs *rtpengine* to convert it to an `image` type media section using the UDPTL
		protocol. The first supported audio codec that was offered will be used to transport
		T.30. Default options for T.38 are used for the generated SDP.

	- `stop`

		Stops a currently active T.38 gateway that was previously engaged using the `decode`
		or `force` flags. This is useful to handle a rejected T.38 offer and revert the
		session back to media passthrough.

	- `no-ECM`

		Disable support for ECM. Support is enabled by default.

	- `no-V.17`

		Disable support for V.17. Support is enabled by default.

	- `no-V.27ter`

		Disable support for V.27ter. Support is enabled by default.

	- `no-V.29`

		Disable support for V.29. Support is enabled by default.

	- `no-V.34`

		Disable support for V.34. Support is enabled by default.

	- `no-IAF`

		Disable support for IAF. Support is enabled by default.

	- `FEC`

		Use UDPTL FEC instead of redundancy. Only useful with `T.38=force` as
		it's a negotiated parameter.

* `supports`

	Contains a list of strings. Each string indicates support for an additional feature
	that the controlling SIP proxy supports. Currently defined values are:

	* `load limit`

		Indicates support for an extension to the *ng* protocol to facilitate certain load
		balancing mechanisms. If *rtpengine* is configured with certain session or load
		limit options enabled (such as the `max-sessions` option), then normally *rtpengine*
		would reply with an error to an `offer` if one of the limits is exceeded. If support
		for the `load limit` extension is indicated, then instead of replying with an error,
		*rtpengine* responds with the string `load limit` in the `result` key of the response
		dictionary. The response dictionary may also contain the optional key `message` with
		an explanatory string. No other key is required in the response dictionary.

* `xmlrpc-callback`

	Contains a string that encodes an IP address (either IPv4 or IPv6) in printable format.
	If specified, then this address will be used as destination address for the XMLRPC timeout
	callback (see `b2b-url` option).

* `media echo` or `media-echo`

	Contains a string to enable a special media echo mode. Recognised values are:

	- `blackhole` or `sinkhole`

		Media arriving from either side of the call is simply discarded
		and not forwarded.

	- `forward`

		Enables media echo towards the receiver of this message (e.g.
		the called party if the message is an `offer` from the caller).
		Media arriving from that side is echoed back to its sender
		(with a new SSRC if it's RTP). Media arriving from the opposite
		side is discarded.

	- `backwards`

		Enables media echo towards the sender of this message (i.e. the
		opposite of `forward`). Media arriving from the other side is
		discarded.

	- `both`

		Enables media echo towards both the sender and the receiver of
		this message.

An example of a complete `offer` request dictionary could be (SDP body abbreviated):

	{ "command": "offer", "call-id": "cfBXzDSZqhYNcXM", "from-tag": "mS9rSAn0Cr",
	"sdp": "v=0\r\no=...", "via-branch": "5KiTRPZHH1nL6",
	"flags": [ "trust address" ], "replace": [ "origin", "session connection" ],
	"address family": "IP6", "received-from": [ "IP4", "10.65.31.43" ],
	"ICE": "force", "transport protocol": "RTP/SAVPF", "media address": "2001:d8::6f24:65b",
	"DTLS": "passive" }

The response message only contains the key `sdp` in addition to `result`, which contains the re-written
SDP body that the SIP proxy should insert into the SIP message.

Example response:

	{ "result": "ok", "sdp": "v=0\r\no=..." }

`answer` Message
----------------

The `answer` message is identical to the `offer` message, with the additional requirement that the
dictionary must contain the key `to-tag` containing the SIP `To` tag. It doesn't make sense to include
the `direction` key in the `answer` message.

The reply message is identical as in the `offer` reply.

`delete` Message
----------------

The `delete` message must contain at least the keys `call-id` and `from-tag` and may optionally include
`to-tag` and `via-branch`, as defined above. It may also optionally include a key `flags` containing a list
of zero or more strings. The following flags are defined:

* `fatal`

	Specifies that any non-syntactical error encountered when deleting the stream
	(such as unknown call-ID) shall
	result in an error reply (i.e. `"result": "error"`). The default is to reply with a warning only
	(i.e. `"result": "ok", "warning": ...`).

Other optional keys are:

* `delete delay`

	Contains an integer and overrides the global command-line option `delete-delay`. Call/branch will be
	deleted immediately if a zero is given. Value must be positive (in seconds) otherwise.

The reply message may contain additional keys with statistics about the deleted call. Those additional keys
are the same as used in the `query` reply.

`list` Message
--------------

The `list` command retrieves the list of currently active call-ids. This list is limited to 32 elements by
default.

* `limit`

	Optional integer value that specifies the maximum number of results (default: 32). Must be > 0. Be
	careful when setting big values, as the response may not fit in a UDP packet, and therefore be invalid.

`query` Message
---------------

The minimum requirement is the presence of the `call-id` key. Keys `from-tag` and/or `to-tag` may optionally
be specified.

The response dictionary contains the following keys:

* `created`

	Contains an integer corresponding to the creation time of this call within the media proxy,
	expressed as seconds since the UNIX epoch.

* `last signal`

	The last time a signalling event (offer, answer, etc) occurred. Also expressed as an integer
	UNIX timestamp.

* `tags`

	Contains a dictionary. The keys of the dictionary are all the SIP tags (From-tag, To-Tag) known
	by *rtpengine* related to this call. One of the keys may be an empty string, which corresponds to
	one side of a dialogue which hasn't signalled its SIP tag yet. Each value of the dictionary is
	another dictionary with the following keys:

	- `created`

		UNIX timestamp of when this SIP tag was first seen by *rtpengine*.

	- `tag`

		Identical to the corresponding key of the `tags` dictionary. Provided to allow for easy
		traversing of the dictionary values without paying attention to the keys.

	- `label`

		The label assigned to this endpoint in the `offer` or `answer` message.

	- `in dialogue with`

		Contains the SIP tag of the other side of this dialogue. May be missing in case of a
		half-established dialogue, in which case the other side is represented by the null-string
		entry of the `tags` dictionary.

	- `medias`

		Contains a list of dictionaries, one for each SDP media stream known to *rtpengine*. The
		dictionaries contain the following keys:

		+ `index`

			Integer, sequentially numbered index of the media, starting with one.

		+ `type`

			Media type as string, usually `audio` or `video`.

		+ `protocol`

			If the protocol is recognized by *rtpengine*, this string contains it.
			Usually `RTP/AVP` or `RTP/SAVPF`.

		+ `flags`

			A list of strings containing various status flags. Contains zero of more
			of: `initialized`, `rtcp-mux`, `DTLS-SRTP`, `SDES`, `passthrough`, `ICE`.

		+ `streams`

			Contains a list of dictionary representing the packet streams associated
			with this SDP media. Usually contains two entries, one for RTP and one for RTCP.
			The keys found in these dictionaries are listed below:

		+ `local port`

			Integer representing the local UDP port. May be missing in case of an inactive stream.

		+ `endpoint`

			Contains a dictionary with the keys `family`, `address` and `port`. Represents the
			endpoint address used for packet forwarding. The `family` may be one of `IPv4` or
			`IPv6`.

		+ `advertised endpoint`

			As above, but representing the endpoint address advertised in the SDP body.

		+ `crypto suite`

			Contains a string such as `AES_CM_128_HMAC_SHA1_80` representing the encryption
			in effect. Missing if no encryption is active.

		+ `last packet`

			UNIX timestamp of when the last UDP packet was received on this port.

		+ `flags`

			A list of strings with various internal flags. Contains zero or more of:
			`RTP`, `RTCP`, `fallback RTCP`, `filled`, `confirmed`, `kernelized,`
			`no kernel support`.

		+ `stats`

			Contains a dictionary with the keys `bytes`, `packets` and `errors`.
			Statistics counters for this packet stream.

* `totals`

	Contains a dictionary with two keys, `RTP` and `RTCP`, each one containing another dictionary
	identical to the `stats` dictionary described above.

A complete response message might look like this (formatted for readability):

          {
            "totals": {
              "RTCP": {
                    "bytes": 2244,
                    "errors": 0,
                    "packets": 22
                  },
              "RTP": {
                   "bytes": 100287,
                   "errors": 0,
                   "packets": 705
                 }
                  },
            "last_signal": 1402064116,
            "tags": {
                  "cs6kn1rloc": {
                  "created": 1402064111,
                  "medias": [
                          {
                      "flags": [
                             "initialized"
                           ],
                      "streams": [
                               {
                           "endpoint": {
                               "port": 57370,
                               "address": "10.xx.xx.xx",
                               "family": "IPv4"
                                   },
                           "flags": [
                                  "RTP",
                                  "filled",
                                  "confirmed",
                                  "kernelized"
                                ],
                           "local port": 30018,
                           "last packet": 1402064124,
                           "stats": {
                                  "packets": 343,
                                  "errors": 0,
                                  "bytes": 56950
                                },
                           "advertised endpoint": {
                                    "family": "IPv4",
                                    "port": 57370,
                                    "address": "10.xx.xx.xx"
                                  }
                               },
                               {
                           "stats": {
                                  "bytes": 164,
                                  "errors": 0,
                                  "packets": 2
                                },
                           "advertised endpoint": {
                                    "family": "IPv4",
                                    "port": 57371,
                                    "address": "10.xx.xx.xx"
                                  },
                           "endpoint": {
                               "address": "10.xx.xx.xx",
                               "port": 57371,
                               "family": "IPv4"
                                   },
                           "last packet": 1402064123,
                           "local port": 30019,
                           "flags": [
                                  "RTCP",
                                  "filled",
                                  "confirmed",
                                  "kernelized",
                                  "no kernel support"
                                ]
                               }
                             ],
                      "protocol": "RTP/AVP",
                      "index": 1,
                      "type": "audio"
                          }
                        ],
                  "in dialogue with": "0f0d2e18",
                  "tag": "cs6kn1rloc"
                      },
                  "0f0d2e18": {
                      "in dialogue with": "cs6kn1rloc",
                      "tag": "0f0d2e18",
                      "medias": [
                        {
                          "protocol": "RTP/SAVPF",
                          "index": 1,
                          "type": "audio",
                          "streams": [
                             {
                               "endpoint": {
                                   "family": "IPv4",
                                   "address": "10.xx.xx.xx",
                                   "port": 58493
                                 },
                               "crypto suite": "AES_CM_128_HMAC_SHA1_80",
                               "local port": 30016,
                               "last packet": 1402064124,
                               "flags": [
                                "RTP",
                                "filled",
                                "confirmed",
                                "kernelized"
                              ],
                               "stats": {
                                "bytes": 43337,
                                "errors": 0,
                                "packets": 362
                              },
                               "advertised endpoint": {
                                  "address": "10.xx.xx.xx",
                                  "port": 58493,
                                  "family": "IPv4"
                                }
                             },
                             {
                               "local port": 30017,
                               "last packet": 1402064124,
                               "flags": [
                                "RTCP",
                                "filled",
                                "confirmed",
                                "kernelized",
                                "no kernel support"
                              ],
                               "endpoint": {
                                   "family": "IPv4",
                                   "port": 60193,
                                   "address": "10.xx.xx.xx"
                                 },
                               "crypto suite": "AES_CM_128_HMAC_SHA1_80",
                               "advertised endpoint": {
                                  "family": "IPv4",
                                  "port": 60193,
                                  "address": "10.xx.xx.xx"
                                },
                               "stats": {
                                "packets": 20,
                                "bytes": 2080,
                                "errors": 0
                              }
                             }
                           ],
                          "flags": [
                           "initialized",
                           "DTLS-SRTP",
                           "ICE"
                         ]
                        }
                      ],
                      "created": 1402064111
                    }
                },
            "created": 1402064111,
            "result": "ok"
          }

`start recording` Message
-------------------------

The `start recording` message must contain at least the key `call-id` and may optionally include `from-tag`,
`to-tag` and `via-branch`, as defined above. The reply dictionary contains no additional keys.

Enables call recording for the call, either for the entire call or for only the specified call leg. Currently
*rtpengine* always enables recording for the entire call and does not support recording only individual
call legs, therefore all keys other than `call-id` are currently ignored.

If the chosen recording method doesn't support in-kernel packet forwarding, enabling call recording
via this messages will force packet forwarding to happen in userspace only.

If the optional 'output-destination' key is set, then its value will be used
as an output file. Note that a filename extension will not be added.

`stop recording` Message
-------------------------

The `stop recording` message must contain the key `call-id` as defined above. The reply dictionary contains
no additional keys.

Disables call recording for the call. This can be sent during a call to immediately stop recording it.

`block DTMF` and `unblock DTMF` Messages
----------------------------------------

These message types must include the key `call-id` in the message. They enable and disable blocking of DTMF
events (RFC 4733 type packets), respectively.

Packets can be blocked for an entire call if only the `call-id` key is present in the message, or can be blocked
directionally for individual participants. Participants can be selected by their SIP tag if the `from-tag` key
is included in the message, they can be selected by their SDP media address if the `address` key is included
in the message, or they can be selected by the user-provided `label` if the `label` key is included in the
message. For an address, it can be an IPv4 or IPv6 address, and any participant that is
found to have a matching address advertised as their SDP media address will have their originating RTP
packets blocked (or unblocked).

Unblocking packets for the entire call (i.e. only `call-id` is given) does not automatically unblock packets for
participants which had their packets blocked directionally, unless the string `all` is included in the `flags`
section of the message.

When DTMF blocking is enabled, DTMF event packets will not be forwarded to the receiving peer.
If DTMF logging is enabled, DTMF events will still be logged to syslog while blocking is enabled. Blocking
of DTMF events can be enabled and disabled at any time during call runtime.

`block media` and `unblock media` Messages
------------------------------------------

Analogous to `block DTMF` and `unblock DTMF` but blocks media packets instead of DTMF packets. DTMF packets
can still pass through when media blocking is enabled. Media packets can be blocked for an entire call, or
directionally for individual participants. See `block DTMF` above for details.

`silence media` and `unsilence media` Messages
----------------------------------------------

Identical to `block media` and `unblock media` except that media packets are
not simply blocked, but rather have their payload replaced with silence audio.
This is only supported for certain trivial audio codecs (i.e. G.711, G.722).

`start forwarding` and `stop forwarding` Messages
-------------------------------------------------

These messages control the recording daemon's mechanism to forward PCM via TCP/TLS. Unlike the call recording
mechanism, forwarding can be enabled for individual participants (directionally) only, therefore these
messages can be used with the same options as the `block` and `unblock` messages above. The PCM forwarding
mechanism is independent of the call recording mechanism, and so forwarding and recording can be started
and stopped independently of each other.

`play media` Message
--------------------

Only available if compiled with transcoding support. The message must contain the key `call-id` and one
of the participant selection keys described under the `block DTMF` message (such as `from-tag`,
`address`, or `label`). Alternatively, the `all` flag can be set to play the media to all involved
call parties.

Starts playback of a provided media file to the selected call participant. The format of the media file
can be anything that is supported by *ffmpeg*, for example a `.wav` or `.mp3` file. It will automatically
be resampled and transcoded to the appropriate sampling rate and codec. The selected participant's first
listed (preferred) codec that is supported will be chosen for this purpose.

Media files can be provided through one of these keys:

* `file`

	Contains a string that points to a file on the local file system. File names can be relative
	to the daemon's working direction.

* `blob`

	Contains a binary blob (string) of the contents of a media file. Due to the limitations of the
	*ng* transport protocol, only very short files can be provided this way, and so this is primarily
	useful for testing and debugging.

* `db-id`

	Contains an integer. This requires the daemon to be configured for accessing a *MySQL* (or *MariaDB*)
	database via (at the minimum) the `mysql-host` and `mysql-query` config keys. The daemon will then
	retrieve the media file as a binary blob (not a file name!) from the database via the provided query.

* `repeat-times`

	Contains an integer. How many times to repeat playback of the media. Default is 1.

In addition to the `result` key, the response dictionary may contain the key `duration` if the length of
the media file could be determined. The duration is given as in integer representing milliseconds.

`stop media` Message
--------------------

Stops the playback previously started by a `play media` message. Media playback stops automatically when
the end of the media file is reached, so this message is only useful for prematurely stopping playback.
The same participant selection keys as for the `play media` message can and must be used.

`play DTMF` Message
-------------------

Instructs *rtpengine* to inject a DTMF tone or event into a running audio stream. A call participant must
be selected in the same way as described under the `play media` message above (including the possibility
of using the `all` flag). The selected call participant is the one generating the DTMF event, not the
one receiving it.

The dictionary key `code` must be present in the message, indicating the DTMF event to be generated. It can
be either an integer with values 0-15, or a string containing a single character
(`0` - `9`, `*`, `#`, `A` - `D`). Additional optional dictionary keys are: `duration` indicating the duration
of the event in milliseconds (defaults to 250 ms, with a minimum of 100 and a maximum of 5000);
`volume` indicating the volume in absolute decibels (defaults to -8 dB, with 0 being the maximum volume and
positive integers being interpreted as negative); and `pause` indicating the pause in between consecutive
DTMF events in milliseconds (defaults to 100 ms, with a minimum of 100 and a maximum of 5000).

This message can be used to implement `application/dtmf-relay` or `application/dtmf` payloads carried
in SIP INFO messages. Multiple DTMF events can be queued up by issuing multiple consecutive
`play DTMF` messages.

If the destination participant supports the `telephone-event` RTP payload type, then it will be used to
send the DTMF event. Otherwise a PCM DTMF tone will be inserted into the audio stream. Audio samples
received during a generated DTMF event will be suppressed.

The call must be marked for DTMF injection using the `inject DTMF` flag used in both `offer` and `answer`
messages. Enabling this flag forces all audio to go through the transcoding engine, even if input and output
codecs are the same (similar to DTMF transcoding, see above).

`statistics` Message
--------------------

Returns a set of general statistics metrics with identical content and format as the `list jsonstats` CLI
command. Sample return dictionary:

	{
	  "statistics": {
	    "currentstatistics": {
	      "sessionsown": 0,
	      "sessionsforeign": 0,
	      "sessionstotal": 0,
	      "transcodedmedia": 0,
	      "packetrate": 0,
	      "byterate": 0,
	      "errorrate": 0
	    },
	    "totalstatistics": {
	      "uptime": "18",
	      "managedsessions": 0,
	      "rejectedsessions": 0,
	      "timeoutsessions": 0,
	      "silenttimeoutsessions": 0,
	      "finaltimeoutsessions": 0,
	      "offertimeoutsessions": 0,
	      "regularterminatedsessions": 0,
	      "forcedterminatedsessions": 0,
	      "relayedpackets": 0,
	      "relayedpacketerrors": 0,
	      "zerowaystreams": 0,
	      "onewaystreams": 0,
	      "avgcallduration": "0.000000"
	    },
	    "intervalstatistics": {
	      "totalcallsduration": "0.000000",
	      "minmanagedsessions": 0,
	      "maxmanagedsessions": 0,
	      "minofferdelay": "0.000000",
	      "maxofferdelay": "0.000000",
	      "avgofferdelay": "0.000000",
	      "minanswerdelay": "0.000000",
	      "maxanswerdelay": "0.000000",
	      "avganswerdelay": "0.000000",
	      "mindeletedelay": "0.000000",
	      "maxdeletedelay": "0.000000",
	      "avgdeletedelay": "0.000000",
	      "minofferrequestrate": 0,
	      "maxofferrequestrate": 0,
	      "avgofferrequestrate": 0,
	      "minanswerrequestrate": 0,
	      "maxanswerrequestrate": 0,
	      "avganswerrequestrate": 0,
	      "mindeleterequestrate": 0,
	      "maxdeleterequestrate": 0,
	      "avgdeleterequestrate": 0
	    },
	    "controlstatistics": {
	      "proxies": [
		{
		  "proxy": "127.0.0.1",
		  "pingcount": 0,
		  "offercount": 0,
		  "answercount": 0,
		  "deletecount": 0,
		  "querycount": 0,
		  "listcount": 0,
		  "startreccount": 0,
		  "stopreccount": 0,
		  "startfwdcount": 0,
		  "stopfwdcount": 0,
		  "blkdtmfcount": 0,
		  "unblkdtmfcount": 0,
		  "blkmedia": 0,
		  "unblkmedia": 0,
		  "playmedia": 0,
		  "stopmedia": 0,
		  "playdtmf": 0,
		  "statistics": 0,
		  "errorcount": 0
		}
	      ],
	      "totalpingcount": 0,
	      "totaloffercount": 0,
	      "totalanswercount": 0,
	      "totaldeletecount": 0,
	      "totalquerycount": 0,
	      "totallistcount": 0,
	      "totalstartreccount": 0,
	      "totalstopreccount": 0,
	      "totalstartfwdcount": 0,
	      "totalstopfwdcount": 0,
	      "totalblkdtmfcount": 0,
	      "totalunblkdtmfcount": 0,
	      "totalblkmedia": 0,
	      "totalunblkmedia": 0,
	      "totalplaymedia": 0,
	      "totalstopmedia": 0,
	      "totalplaydtmf": 0,
	      "totalstatistics": 0,
	      "totalerrorcount": 0
	    }
	  },
	  "result": "ok"
	}

`publish` Message
-----------------

Similar to an `offer` message except that it is used outside of an offer/answer
scenario. The media described by the SDP is published to *rtpengine* directly,
and other peer can then subscribe to the published media to receive a copy.

The message must include the key `sdp` which should describe `sendonly` media;
and the key `call-id` and `from-tag` to identify the publisher. Most other keys
and options supported by `offer` are also supported for `publish`.

The reply message will contain an answer SDP in `sdp`, but unlike with `offer`
this is not a rewritten version of the received SDP, but rather a `recvonly`
answer SDP generated by *rtpengine* locally. Only one codec for each media
section will be listed, and by default this will be the first supported codec
from the published media. This can be influenced with the `codec` options
described above.

`subscribe request` Message
---------------------------

This message is used to request subscription (i.e. receiving a copy of the
media) to an existing call participant, which must have been created either
through the offer/answer mechanism, or through the publish mechanism.

The call participant is selected in the same way as described under `block
DTMF` except that one call participant must be selected (i.e. the `all` keyword
cannot be used). This message then creates a new call participant, which
corresponds to the subscription. This new call participant will be identified
by a newly generated unique tag, or by the tag given in the `to-tag` key. If a
label is to be set for the newly created subscription, it can be set through
`set-label`.

The reply message will contain a sendonly offer SDP in `sdp` which by default
will mirror the SDP of the call participant being subscribed to. This offer SDP
can be manipulated with the same flags as used in an `offer` message, including
the option to manipulate the codecs. The reply message will also contain the
`from-tag` (corresponding to the call participant being subscribed to) and the
`to-tag` (corresponding to the subscription, either generated or taken from the
received message).

`subscribe answer` Message
--------------------------

This message is expected to be received after responding to a `subscribe
request` message. The message should contain the same `from-tag` and `to-tag`
is the reply to the `subscribe request` (although `label` etc can also be used
instead of the `from-tag`), as well as the answer SDP in `sdp`.

By default, the answer SDP must accept all codecs that were presented in the
offer SDP (given in the reply to `subscribe request`). If not all codecs were
accepted, then the `subscribe answer` will be rejected. This behavious can be
changed by including the `allow transcoding` flag in the message. If this flag
is present, then the answer SDP will be accepted as long as at least one valid
codec is present, and the media will be transcoded as required. This also holds
true if some codecs were added for transcoding in the `subscribe request`
message, which means that `allow transcoding` must always be included in
`subscribe answer` if any transcoding is to be allowed.

The reply message will simply indicate success or failure. If successful, media
forwarding will start to the endpoint given in the answer SDP.

`unsubscribe` Message
---------------------

This message is a counterpart to `subsscribe answer` to stop an established
subscription. The subscription to be stopped is identified by `from-tag` and
`to`tag`.
