https://www.netmeister.org/blog/ops-lessons.html


* Email is the worst monitoring and alerting mechanism except for all the others.
* Absence of a signal is itself a signal.
* The severity of an incident is measured by the number of rules broken in resolving it.
* The mobile hotspot you're paying for so you can leave your house while you're oncall only works at home and in the office.
* The only other person who knows how this works is also on vacation.
* If a post-mortem follow-up task is not picked up within a week, it's unlikely to be completed at all.
* That janky script you put together during the outage -- the one that uses expect(1) and 'ssh -t -t' -- now is the foundation of the entire team's toolchest.
* NTP being off may not be a root cause, but it sure didn't help.
* UTC or GTFO.
* Your infrastructure uses a lot more self-signed certificates than you think. A lot more. In places that make you weep.
* Self-signed certificates beget long lived certs, which beget lack of certificate validity monitoring, which begets curl -k, which begets a lack of certificate deployment automation, which begets self-signed certificates.
* For any N applications, at most N/2+1 use the same certificate bundle.
* The system you're troubleshooting doesn't use the one the tool you're troubleshooting it with does.
* An API without a reference implementation and command-line client is called a gray box.
* Restricted shells are not as restricted as you think.
* Very few operations are truly idempotent.
* "Asserting state" beats "monitoring for compliance" any day.
* One in a Million is next Tuesday.
* People give talks at conferences not to convince others that their work is awesome and totally worth the time and effort they put in, but themselves.
* There is no cloud, it's just someone else's computer.It's ok to use shell for complex stuff; it often times is easier, faster, and still less of a mess than juggling libraries and dependencies.
* There's nothing wrong with Perl.
* Ok, we all at times keep adding $, {, }, and @ in random places trying to make things work, but still.
* Serverless isn't.
* Y38K is already here, it's just not evenly distributed.
* If you determine "human error" as the root cause, then you're doing it wrong.
* Your network team has a way into the network that your security team doesn't know about.
* And don't even as much as mention the serial console and IPMI networks, but boy are you glad you have 'em.
* Blocking TCP port 53 traffic leads to very strange failures. Don't.
* Somewhere in your infrastructure a service you didn't know uses DNS for endpoint discovery in a very surprising way.
* Do. Not. Monkey. Around. With. /etc/hosts.
* If you break it, you own it - for now; if you fix it, you own it - forever.
* Turning it off and on again is actually quite a reasonable way to fix many things.
* A README.md in git is no substitute for a manual page that's shipped with your tool.
* A search for a document you know exists will only turn up links to documents referencing but not actually linking to the one you're looking for.
* The document you're looking for was marked as obsolete and not migrated to the new content management solution.
* Connected hot water pipes.Sure, your current content management system sucks, but it's still better than the one you're moving to.
* Nobody knows how git works; everybody simply rm -fr && git checkout's periodically.
* There are very few network restrictions creative and determined use of ssh(1) port forwarding can't overcome.
* This is both incredibly useful and concerning.
* It is tempting to jump right into implementing a solution when the right thing may well be to not do the thing that requires the solution in the first place.
* Turning things off permanently is surprisingly difficult.
* "Ancient" is a very relative term when it comes to software and protocols.
* "Obsolete" doesn't mean it's not in use and relied on.
* The sets of systems online before and after a data center power outage only intersect. Some of the old systems coming online will immediately cause a different outage.
* Some of your most critical services are kept alive by a handful of people whose job description does not mention those services at all.
* After the initial "down for everybody or just me ermahgehrd Slack is down" drop, productivity increases linearly throughout the duration of the outage.
* You're bound by the CAP theorem much more often than you may think. Halting Problem's a bitch, too.
* Eventual consistency doesn't help when the system you're debugging hasn't converged yet.
* The source you're looking at is not the code running in production.
* strace(1)/ktrace(1) doesn't lie.
* Unless somebody's been playing LD_PRELOAD games.
* Schrödinger's Backup -- "The condition of any backup is unknown until a restore is attempted." -- is overly optimistic.
* There's an xkcd for the precise situation you find yourself in. (There's also one for at least half of these.)
* At some point in your career you will implement half of kerberos. Poorly.
* Any sufficiently successful product launch is indistinguishable from a DDoS; any sufficiently advanced user indistinguishable from an attacker.
* Debugging any sufficiently complex open source product is indistinguishable from reverse engineering a black box.
* "We've always done it this way." is not a good reason by itself, but there's bound to be one for why.
* That reason may or may not be valid any longer, however.
* Circles of Hell from Dante's InfernoA junior engineer asking "why" and pointing out the docs don't reflect reality is at least as valuable as the senior engineer working blindly off tribal knowledge.
* Your herculean efforts to upgrade the OS across your entire fleet completed just in time for the EOL announcement of the version you upgraded to.
* This phenomenon was first described in Dante's Inferno as the Ninth Circle of Hell, Ring Four, aka RedHat Canto XXXIV.
* Containers create at least as many problems as they solve.
* The most ninja move the expert you hired for that third party black box product you rely on is to say "Let me ping the support team".
* Somewhere, somebody ran into this exact problem, but they never bothered to post a solution.
* That completely automated solution you set up requires at least three manual steps you didn't document.
* CAPEX budget always increases, OPEX budget always decreases.
* CAPEX costs can be reasonably estimated, OPEX costs can only be ballparked.
* Doubling your time estimate in the hopes of beating expectations won't work because your manager takes your estimate, has a hardy laugh, and then resets it back to what they already promised upchain.
* Your quarterly planning means bubkes when the next re-org rolls around.
* Most of your actual work is not covered by your OKRs.
* Recursively applying the Pareto Principle is a surprisingly accurate way to gauge your low hanging fruit, determine your high impact objectives, and ballpark your required effort.
* Although, to be honest, it only works in about 80% of cases.
* Management will always happily spend $$$ on outside consultants to tell them what you've been saying for years.
* Management will much rather invest in inventing a new, square wheel than fixing an old round one.
* In any organization practicing continuous integration, half of all commits are to fake out CI tests.
* Good software development practices do not always translate well to ops and friends.
* Mandatory code reviews do not automatically improve code quality nor reduce the frequency of incidents.
* Every new paradigm tends to mostly add layers of abstractions; cutting through them and identifying what basic principles continue to apply is half the battle.
* OSI stack with layers 8 (Financial) and 9 (Political) added Real change can only be implemented above layer 7.
* "Prod" is just another name for "staging".
* Your source of truth lies.
* Also: it's incomplete.
* pcap or it didn't happen.
* grep(1) > Splunk (there, I said it)
* Multithreading is rarely worth the added complexity.
* Parallelism is not Concurrency.
* Simplicity is King.
* Nobody knows what exactly it is you do.


