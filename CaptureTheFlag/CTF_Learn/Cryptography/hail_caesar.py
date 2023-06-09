# Exercise: https://ctflearn.com/challenge/952
# help_1: https://stackoverflow.com/questions/227459/how-to-get-the-ascii-value-of-a-character
#
# Comment: Script for decoding Cesar cripting. It will bruteforce all ascii combination of text.
# 
import base64
import sys

sys.path.append('../../../modules/crypto/')
import caesar_ascii_crypto

base64_encoded_message = 'SWYgeW91IGFyZSBoYXZpbmcgdHJvdWJsZSBzb2x2aW5nIHRoaXMgY2hhbGxlbmdlLCBwbGVhc2Ug.c29sdmUgbXkgb3RoZXIKY2hhbGxlbmdlcyBmaXJzdDoKUnViYmVyRHVjawpTbm93Ym9hcmQKUGlr.ZXNQZWFrCkdhbmRhbGZUaGVXaXNlCgpUaGUgY2hhbGxlbmdlcyBhcmUgZGVzaWduZWQgdG8gYmUg.aW5jcmVhc2luZyBpbiBkaWZmaWN1bHR5IGFuZCB0aGlzIEhhaWxDYWVzYXIgY2hhbGxlbmdlIGlz.IHRoZSBuZXh0CmNoYWxsZW5nZSBpbiB0aGUgc2VyaWVzLgoKTXkgVHdpdHRlciBETSBpcyBvcGVu.IEBrY2Jvd2h1bnRlciBidXQgcGxlYXNlIG9ubHkgcGluZyBtZSBpZiB5b3UgaGF2ZSBzb2x2ZWQg.dGhlIGFib3ZlIGNoYWxsZW5nZXMgZmlyc3QuCgpJZiB5b3UgYXJlIG5ldyB0byB0aGUganBlZyBm.aWxlIGZvcm1hdCBwbGVhc2UgcmVhZCB0aGlzOgpodHRwczovL2Rldi5leGl2Mi5vcmcvcHJvamVj.dHMvZXhpdjIvd2lraS9UaGVfTWV0YWRhdGFfaW5fSlBFR19maWxlcwoKSWYgeW91IGFyZSBuZXcg.dG8gaGFja2luZyBhbmQgYXJlIHN0aWxsIGxlYXJuaW5nIGFib3V0IGJpdHMgYW5kIGJ5dGVzIHBs.ZWFzZSB3YXRjaCB0aGlzIHZpZGVvOgpodHRwczovL3d3dy55b3V0dWJlLmNvbS93YXRjaD92PXRM.ZHZFT2FtM3NrCgp4b3JwZCBoYXMgYSBsb3Qgb2YgZnJlZSB2aWRlb3MgdGhhdCB0ZWFjaCBpbXBv.cnRhbnQgY29tcHV0ZXIgc2NpZW5jZSAvIGhhY2tpbmcgY29uY2VwdHMuCgpOb3RlIHRoYXQgb2Z0.ZW4gbXkgY2hhbGxlbmdlcyBjb21iaW5lIGZvcmVuc2ljcyBhbmQgc29tZSBhc3BlY3Qgb2YgY3J5.cHRvZ3JhcGh5LgoKSGF2ZSBmdW4hCmtjYm93aHVudGVyCgoK.'
base64_decoded_message = base64.b64decode(base64_encoded_message).decode('utf-8')

encoded_message = '2m{y!"%w2''z{&o2UfX~ws%!._s+{ (&@Vwu{ (&@_w%{v{(&0'


def print_output(text_to_print):
    print()
    print('-- ================================================================== --')
    print(text_to_print)
    print('-- ================================================================== --')


print_output(base64_decoded_message)
print_output('CAESAR BRUTEFORCE OUTPUT')

bruteforce_caesar = caesar_ascii_crypto.bruteforce_decrypt(encoded_message)
for i, decrypted in enumerate(bruteforce_caesar):
    print_output(str(i) + '. ' + decrypted)
