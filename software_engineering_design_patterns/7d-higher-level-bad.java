// If there is a LOADING readRpc using the same session
// as PKHash pointed to by assignPos, and the last PKHash
// in that readRPC is smaller than current assigning
// PKHash, then we put assigning PKHash into that readRPC.
int readActiveRpcId = RPC_ID_NOT_ASSIGNED;
for (int i = 0; i < NUM_READ_RPC; i++) {
  if (session == readRpc[i].session
  && readRpc[i].status == LOADING
  && readRpc[i].maxPos < assignPos
  && readRpc[i].numHashes < MAX_PKHASHES_PERRPC) {
    readActiveRpcId = i;
    break;
  }
}
