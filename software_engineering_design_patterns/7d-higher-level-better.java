// Try to append the current key hash onto an existing
// RPC to the desired server that hasn't been sent yet.
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
