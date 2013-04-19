from util import Enumerator

class AuthorizationOptions(Enumerator):
    """The bits represented by these masks instruct the Security Server how to proceed with the function in which you pass them. Set all unused bits to 0 to allow for future expansion."""
    kAuthorizationFlagDefaults__doc__ = """If no bits are set, none of the following features are available."""
    kAuthorizationFlagDefaults = 0
    kAuthorizationFlagInteractionAllowed__doc__ = """If the bit specified by this mask is set, you permit the Security Server to interact with the user when necessary."""
    kAuthorizationFlagInteractionAllowed = (1 << 0)
    kAuthorizationFlagExtendRights__doc__ = """If the bit specified by this mask is set, the Security Server attempts to grant the rights requested. Once the Security Server denies one right, it ignores the remaining requested rights."""
    kAuthorizationFlagExtendRights = (1 << 1)
    kAuthorizationFlagPartialRights__doc__ = """If the bit specified by this mask and the kAuthorizationFlagExtendRights mask are set, the Security Server grants or denies rights on an individual basis and all rights are checked."""
    kAuthorizationFlagPartialRights = (1 << 2)
    kAuthorizationFlagDestroyRights__doc__ = """If the bit specified by this mask is set, the Security Server revokes authorization from the process as well as from any other process that is sharing the authorization. If the bit specified by this mask is not set, the Security Server revokes authorization from the process but not from other processes that share the authorization."""
    kAuthorizationFlagDestroyRights = (1 << 3)
    kAuthorizationFlagPreAuthorize__doc__ = """If the bit specified by this mask is set, the Security Server preauthorizes the rights requested."""
    kAuthorizationFlagPreAuthorize = (1 << 4)
    kAuthorizationFlagNoData__doc__ = """Private bits. Do not use."""
    kAuthorizationFlagNoData = (1 << 20)

class AuthorizationRights(Enumerator):
    """Defines values the Security Server sets in an authorization item's flag field."""
    kAuthorizationFlagCanNotPreAuthorize__doc__ = """Indicates the Security Server could not preauthorize the right."""
    kAuthorizationFlagCanNotPreAuthorize = (1 << 0)

class AuthorizationLength(Enumerator):
    """Defines the byte length of the external authorization reference."""
    kAuthorizationExternalFormLength__doc__ = """Indicates, in number of bytes, the length of the array in the AuthorizationExternalForm structure."""
    kAuthorizationExternalFormLength = 32

class AuthorizationRightTags(Enumerator):
    """Defines some of the supported rights tags to be used in the Authorization API"""
    __basetype__ = str
    kAuthorizationRightExecute__doc__ = """The name of the AuthorizationItem that should be passed into the rights when preauthorizing for a call to AuthorizationExecuteWithPrivileges()."""
    kAuthorizationRightExecute = "system.privilege.admin"

class AuthorizationEnvironmentTags(Enumerator):
    """These tags are possible values for the name field of an authorization item. This is not an all-inclusive set. You determine the name of the right to request. These environment tags are for future use."""
    __basetype__ = str
    kAuthorizationEnvironmentUsername__doc__ = """Specifies a user name."""
    kAuthorizationEnvironmentUsername = "username"
    kAuthorizationEnvironmentPassword__doc__ = """Specifies a password."""
    kAuthorizationEnvironmentPassword = "password"
    kAuthorizationEnvironmentShared__doc__ = """Specifies a shared right."""
    kAuthorizationEnvironmentShared = "shared"
    kAuthorizationRightExecute__doc__ = """Specifies the name of the right associated with the function AuthorizationExecuteWithPrivileges."""
    kAuthorizationRightExecute = "system.privilege.admin"

class AuthorizationErrors(Enumerator):
    errAuthorizationSuccess                 = 0
    errAuthorizationSuccess__doc__ = """The operation completed successfully"""
    errAuthorizationInvalidSet              = -60001
    errAuthorizationInvalidSet__doc__ = """The set parameter is invalid"""
    errAuthorizationInvalidRef              = -60002
    errAuthorizationInvalidRef__doc__ = """The authorization parameter is invalid"""
    errAuthorizationInvalidTag              = -60003
    errAuthorizationInvalidTag__doc__ = """The tag parameter is invalid"""
    errAuthorizationInvalidPointer          = -60004
    errAuthorizationInvalidPointer__doc__ = """The authorizedRights parameter is invalid"""
    errAuthorizationDenied                  = -60005
    errAuthorizationDenied__doc__ = """The authorization was denied"""
    errAuthorizationCanceled                = -60006
    errAuthorizationCanceled__doc__ = """The authorization was cancled by the user"""
    errAuthorizationInteractionNotAllowed   = -60007
    errAuthorizationInteractionNotAllowed__doc__ = """The authorization was denied since no user interaction was possible"""
    errAuthorizationInternal                = -60008
    errAuthorizationInternal__doc__ = """Something else went wrong"""
    errAuthorizationExternalizeNotAllowed   = -60009
    errAuthorizationExternalizeNotAllowed__doc__ = """Authorization externalization denied"""
    errAuthorizationInternalizeNotAllowed   = -60010
    errAuthorizationInternalizeNotAllowed__doc__ = """Authorization internalization denied"""
    errAuthorizationInvalidFlags            = -60011
    errAuthorizationInvalidFlags__doc__ = """Invalid option flag(s)"""
    errAuthorizationToolExecuteFailure      = -60031
    errAuthorizationToolExecuteFailure__doc__ = """Cannot execute privileged tool"""
    errAuthorizationToolEnvironmentError    = -60032
    errAuthorizationToolEnvironmentError__doc__ = """Privileged tool environment error""" 
    errAuthorizationBadAddress              = -60033
    errAuthorizationBadAddress__doc__ = """Invalid socket address requested"""
    
kAuthorizationEmptyEnvironment = None

_globals = globals()
for _v in _globals.values():
    if isinstance(_v, type) and issubclass(_v, Enumerator):
        _globals.update(_v.__keys__)
del _globals, _v
