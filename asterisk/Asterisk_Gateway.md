# What Is A VoIP Gateway?

A VoIP gateway is used to build a bridge between the worlds of legacy telephony and the VoIP.  Gateways are typically used to connect legacy phone systems (PBXs or ACDs) with VoIP resources, or to connect modern VoIP phone systems with legacy phone lines.

Adding VoIP to a legacy PBX system is a great way to add features and reduce costs.  The gateway connects to the legacy system through either analog or digital trunk ports.  The PBX sees the gateway as either the phone company or as another networked PBX.  Calls from the PBX to the outside world are converted into VoIP calls and sent over the Internet to a VoIP service provider or other VoIP peers.  Calls coming from VoIP sources are converted into the appropriate legacy protocol and delivered to the PBX.

Using a gateway to connect a VoIP phone system to traditional phone lines makes sense in situations where SIP trunks are not available or where your application requires the reliability of the PSTN. It also makes it easy to build redundant systems. The gateway normally communicates with a primary IP PBX. In the event of a failure on the primary, the gateway can communicate with a backup system.

Other uses for VoIP gateways include staged migrations, where the gateway acts as a bridge between the PSTN, a legacy PBX and a new IP PBX.  In this case, the PSTN trunks are connected to one interface on the gateway.  Another interface connects to the trunk port on the legacy PBX.  The new IP PBX is integrated over a VoIP protocol (generally SIP). The gateway directs some incoming calls to the legacy PBX and others to the IP PBX.  It also passes calls between the two PBXs.  This allows some department or other subdivisions of the company to remain on the legacy system while others move to the IP system.

## Key Facts & Features
Gateways come in several formats. Analog gateways convert between VoIP protocols and traditional analog phone lines and/or phones. Digital gateways convert between VoIP and various kinds of digital phone services: T1, E1, PRI and/or BRI, depending on the gateway.

Gateways can typically connect to multiple VoIP endpoints (devices or services), which allows PSTN resources to be shared between multiple IP communications systems.

The routing functions built into a gateway allow it to intelligently adapt calls from one medium to another. For example, they can add or remove digits in the dial string when passing a call.  They can also recognize various patterns and route them across different interfaces.

Gateways can be used to convert VoIP calls from one code to another, a process known as transcoding. This can be useful when bridging multiple VoIP solutions together.  VoIP calls over the Internet do require a solid Internet connection.  Run a VoIP network test as a simple diagnostic tool to identify the jitter, bandwidth, and latency on the Internet connection.

## Key Benefits
Gateways can extend the life of legacy equipment by “VoIP enabling” it.  This can include replacing traditional trunk lines with SIP trunks or routing some subset of traffic over VoIP to a remote PBX or gateway — a process known as toll bypass.

Gateways enable flexibility. Rather than moving from a traditional PBX to an IP PBX in one step, a company can stage the migration using the gateway as a bridge between the two systems.

## Asterisk As A Gateway
Asterisk can be used to build a gateway using a standard computer and one or more telephony interface cards.  Alternately, Sangoma offers a line of VoIP gateways. In either case, the end product is significantly more flexible and significantly less expensive than legacy gateway products.  Asterisk’s modular, multi-protocol architecture is particularly well suited to building gateways.

