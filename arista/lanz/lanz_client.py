#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/env python
# Copyright (c) 2011 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys, socket, time, optparse
import Lanz_pb2
#from google.protobuf.internal import decoder

LANZ_PORT = 50001

def getTimeFromTS( ts ):
   usecs = ts % 100001 # 10 usec precision
   secs = ts / 100000
   dateTimeStr = time.ctime( secs )
   pos = len(dateTimeStr) - 5
   return dateTimeStr[:pos] + "." + str(usecs) + dateTimeStr[pos:]

def getTxLatency ( latency ):
	latency = latency/1000.0 
	return str(latency)

def getCongestionEntryType( entryType ):
	entType=''
	if entryType == Lanz_pb2.CongestionRecord.START:
		entType = 'Start'
	elif entryType == Lanz_pb2.CongestionRecord.UPDATE: 
		entType = 'Update'
	elif entryType == Lanz_pb2.CongestionRecord.END: 
		entType = 'End'
	return entType

def getGlobalBufferEntryType( entryType ):
	entType=''
	if entryType == Lanz_pb2.GlobalBufferUsageRecord.LOW:
		entType = 'Low'
	elif entryType == Lanz_pb2.GlobalBufferUsageRecord.UPDATE: 
		entType = 'Update'
	elif entryType == Lanz_pb2.GlobalBufferUsageRecord.HIGH: 
		entType = 'High'
	return entType

def interpretLanzRecord( lanzRecord, printCsv=False ):
   if lanzRecord.HasField('configRecord'):
      print "ConfigRecord:"
      rec = lanzRecord.configRecord
      print "   timestamp:", getTimeFromTS( rec.timestamp )
      print "   lanzVersion:", rec.lanzVersion
      print "   numOfPorts:", rec.numOfPorts
      print "   segmentSize:", rec.segmentSize
      print "   maxQueueSize:", rec.maxQueueSize
      if rec.HasField('globalUsageHighThreshold'):
         print "   globalUsageHighThreshold:", rec.globalUsageHighThreshold
      if rec.HasField('globalUsageLowThreshold'):
         print "   globalUsageLowThreshold:", rec.globalUsageLowThreshold
      if rec.HasField('globalUsageReportingEnabled'):
         print "   globalUsageReportingEnabled:", rec.globalUsageReportingEnabled

      portCfgNum = 1
      for rec in rec.portConfigRecord:
         print "   PortConfigRecord %d:" % portCfgNum
         print "      intfName:", rec.intfName
         print "      switchId:", rec.switchId
         print "      portId:", rec.portId
         print "      internalPort:", rec.internalPort
         print "      highThreshold:", rec.highThreshold
         print "      lowThreshold:", rec.lowThreshold
         portCfgNum += 1

   if lanzRecord.HasField('congestionRecord'):
      rec = lanzRecord.congestionRecord
      if not printCsv:
         print "CongestionRecord:"
         print "   timestamp:", getTimeFromTS( rec.timestamp )
         print "   intfName:", rec.intfName
         print "   switchId:", rec.switchId
         print "   portId:", rec.portId
         print "   queueSize:", rec.queueSize

         if rec.HasField('entryType'):
         	print "   entryType:", getCongestionEntryType( rec.entryType )
         if rec.HasField('trafficClass'):
         	print "   trafficClass:", rec.trafficClass
         if rec.HasField('timeOfMaxQLen'):
         	print "   timeOfMaxQLen:", rec.timeOfMaxQLen
         if rec.HasField('txLatency'):
         	print "   txLatency:", getTxLatency( rec.txLatency )
         if rec.HasField('qDropCount'):
         	print "   qDropCount:", rec.qDropCount
      else:
         recordStr=''
         if rec.HasField('entryType'):
            recordStr += getCongestionEntryType( rec.entryType ) + ','
         else :
            recordStr += 'N/A,'; 
         if rec.HasField('trafficClass'):
            recordStr += str( rec.trafficClass ) + ','
         else :
            recordStr += 'N/A,'; 
         if rec.HasField('timeOfMaxQLen'):
            recordStr += str( rec.timeOfMaxQLen ) + ','
         else :
            recordStr += 'N/A,'; 
         if rec.HasField('txLatency'):
            recordStr += getTxLatency( rec.txLatency ) + ','
         else :
            recordStr += 'N/A,'; 
         if rec.HasField('qDropCount'):
            recordStr += str( rec.qDropCount ) 
         else :
            recordStr += 'N/A'; 
         print "%d,%s,%d,%d,%d,%s" % ( rec.timestamp, rec.intfName, rec.switchId,
                                    rec.portId, rec.queueSize, recordStr )

   if lanzRecord.HasField('globalBufferUsageRecord'):
      rec = lanzRecord.globalBufferUsageRecord
      if not printCsv:
         print "GlobalBufferUsageRecord:"
         if rec.HasField('entryType'):
            print "   entryType:", getGlobalBufferEntryType( rec.entryType )
         if rec.HasField('timestamp'):
            print "   timestamp:", getTimeFromTS( rec.timestamp )
         if rec.HasField('bufferSize'):
            print "   bufferSize:", rec.bufferSize
         if rec.HasField('duration'):
            print "   duration:", rec.duration
      else:
         recordStr=''
         if rec.HasField('entryType'):
            recordStr += getGlobalBufferEntryType( rec.entryType ) + ','
         else :
            recordStr += 'N/A,'; 
         if rec.HasField('timestamp'):
            recordStr += str( rec.timestamp ) + ','
         else :
            recordStr += 'N/A,'; 
         if rec.HasField('bufferSize'):
            recordStr += str( rec.bufferSize ) + ','
         else :
            recordStr += 'N/A,'; 
         if rec.HasField('duration'):
  	         recordStr += str( rec.duration)
         else :
            recordStr += 'N/A'; 
         print recordStr

   if lanzRecord.HasField('errorRecord'):
      print "ErrorRecord:"
      rec = lanzRecord.errorRecord
      print "   timestamp:", getTimeFromTS( rec.timestamp )
      print "   message:", rec.errorMessage
      sys.exit()

def readCodedStream( fileDescriptor, bytesToRead, waitTime=0.2 ):
   errCount = 0
   result = ''
   bytesRemaining = bytesToRead
   while bytesRemaining != 0:
      try:
         str = fileDescriptor.recv( bytesRemaining )
      except KeyboardInterrupt:
         raise 
      except:
         if errCount == 5:
            raise RuntimeError( "Read partial buffer of size %d in an attempt to "\
                                "read %d bytes. Timeout." %
                                ( len( result ), bytesToRead ) )
         else:
            errCount += 1
            time.sleep( waitTime )
      else:
         if str == '':
            errCount += 1
            time.sleep( waitTime )

         if errCount == 5:
            raise RuntimeError( "Received incomplete record. Server connection "
                                "might be broken!!" )
         else:
            result += str
            bytesRemaining -= len( str )
   return result

def connectToServer( serverIp ):
   # Returns both IPv4 and IPv6 results. Connecting to either of them should suffice
   for result in socket.getaddrinfo( serverIp, LANZ_PORT, socket.AF_INET,
                                     socket.SOCK_STREAM ):
      af, sockType, proto, canonName, srvAddr = result
      try:
         sock = socket.socket( af, sockType, proto )
      except socket.error, msg:
         print "Creating socket failed with -", msg
         continue
      # Set timeout for establishing connection with the switch
      sock.settimeout(5)
      try:
         # srvAddr is a tuple of <ip-addr, port>
         sock.connect( srvAddr )
      except socket.error, msg:
         print "Connecting to '%s' - %s" % (serverIp, msg)
         sock.close()
         continue
      else:
         break
   else:
      print "Failed to connect to the server."
      return None

   sock.setblocking( True )
   print "Connected to the Lanz server -", srvAddr[0]
   return sock

def parseArgs( argv ):
   op = optparse.OptionParser( usage="%prog --host <switchIp> --csv" )
   op.add_option( "-i", "--host", action="store",
                  help="Ip address or Hostname of the switch on which Lanz"\
                        "streaming is enabled",
                  default="localhost" )
   op.add_option( "--csv", action="store_true",
                  help="Print congestion records in CSV format",
                  default=False )
   opts, args = op.parse_args( argv )
   serverIp = opts.host
   csvEnabled = opts.csv
   return (serverIp, csvEnabled)

def main(argv):
   print "Welcome to the Python based client of Lanz Streaming\n"

   (serverIp, printInCsv) = parseArgs( argv )

   sock = connectToServer( serverIp )
   if sock is None:
      sys.exit()

   # At the rate at which the records are generated, it may be required
   # for the client to have large receive-buffer in its socket
   #sock.setsockopt( socket.SOL_SOCKET, socket.SO_RCVBUF, 4194304 )

   lanzRecord = Lanz_pb2.LanzRecord()

   # Start the loop for receiving lanz stream
   print "\nReady to handle message from server..."
   while True:
      # Size (integer) doesn't take more than 4 bytes
      try:
         tl = readCodedStream( sock, 4 )
      except:
         raise

      # Parse the record and decode the record size
      recordSize = 0
      shift = 0
      pos = 0
      while True:
         num = ord( tl[ pos ] )
         pos += 1
         recordSize |= ( ( num & 0x7f ) << shift )
         shift += 7
         if not ( num & 0x80 ):
            break

      # We might have over-read the stream. So, adjust the size of buffer
      # yet to be read from the socket
      recordSize -= ( 4 - pos )

      # Consider the over-read part to be part of the actual record
      gpbStream = tl[ pos: ]

      # Read the remaining record
      try:
         gpbStream += readCodedStream( sock, recordSize )
      except:
         raise

      lanzRecord.ParseFromString( gpbStream )

      interpretLanzRecord( lanzRecord, printInCsv )

if __name__ == "__main__":
   try:
      main( sys.argv[1:] )
   except KeyboardInterrupt:
      print 'Good bye!!!!'
      sys.exit(0)

