# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except ImportError:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class kb_SetUtilities(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://ci.kbase.us/services/auth/api/legacy/KBase/Sessions/Login',
            service_ver='release',
            async_job_check_time_ms=100, async_job_check_time_scale_percent=150, 
            async_job_check_max_time_ms=300000):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = service_ver
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc,
            async_job_check_time_ms=async_job_check_time_ms,
            async_job_check_time_scale_percent=async_job_check_time_scale_percent,
            async_job_check_max_time_ms=async_job_check_max_time_ms)

    def KButil_Localize_GenomeSet(self, params, context=None):
        """
        :param params: instance of type "KButil_Localize_GenomeSet_Params"
           (KButil_Localize_GenomeSet() ** **  Method for creating Genome Set
           with all local Genomes) -> structure: parameter "workspace_name"
           of type "workspace_name" (** The workspace object refs are of
           form: ** **    objects = ws.get_objects([{'ref':
           params['workspace_id']+'/'+params['obj_name']}]) ** ** "ref" means
           the entire name combining the workspace id and the object name **
           "id" is a numerical identifier of the workspace or object, and
           should just be used for workspace ** "name" is a string identifier
           of a workspace or object.  This is received from Narrative.),
           parameter "input_ref" of type "data_obj_ref", parameter
           "output_name" of type "data_obj_name"
        :returns: instance of type "KButil_Localize_GenomeSet_Output" ->
           structure: parameter "report_name" of type "data_obj_name",
           parameter "report_ref" of type "data_obj_ref"
        """
        return self._client.run_job('kb_SetUtilities.KButil_Localize_GenomeSet',
                                    [params], self._service_ver, context)

    def KButil_Localize_FeatureSet(self, params, context=None):
        """
        :param params: instance of type "KButil_Localize_FeatureSet_Params"
           (KButil_Localize_FeatureSet() ** **  Method for creating Feature
           Set with all local Genomes) -> structure: parameter
           "workspace_name" of type "workspace_name" (** The workspace object
           refs are of form: ** **    objects = ws.get_objects([{'ref':
           params['workspace_id']+'/'+params['obj_name']}]) ** ** "ref" means
           the entire name combining the workspace id and the object name **
           "id" is a numerical identifier of the workspace or object, and
           should just be used for workspace ** "name" is a string identifier
           of a workspace or object.  This is received from Narrative.),
           parameter "input_ref" of type "data_obj_ref", parameter
           "output_name" of type "data_obj_name"
        :returns: instance of type "KButil_Localize_FeatureSet_Output" ->
           structure: parameter "report_name" of type "data_obj_name",
           parameter "report_ref" of type "data_obj_ref"
        """
        return self._client.run_job('kb_SetUtilities.KButil_Localize_FeatureSet',
                                    [params], self._service_ver, context)

    def KButil_Merge_FeatureSet_Collection(self, params, context=None):
        """
        :param params: instance of type
           "KButil_Merge_FeatureSet_Collection_Params"
           (KButil_Merge_FeatureSet_Collection() ** **  Method for merging
           FeatureSets) -> structure: parameter "workspace_name" of type
           "workspace_name" (** The workspace object refs are of form: ** ** 
           objects = ws.get_objects([{'ref':
           params['workspace_id']+'/'+params['obj_name']}]) ** ** "ref" means
           the entire name combining the workspace id and the object name **
           "id" is a numerical identifier of the workspace or object, and
           should just be used for workspace ** "name" is a string identifier
           of a workspace or object.  This is received from Narrative.),
           parameter "input_refs" of type "data_obj_ref", parameter
           "output_name" of type "data_obj_name", parameter "desc" of String
        :returns: instance of type
           "KButil_Merge_FeatureSet_Collection_Output" -> structure:
           parameter "report_name" of type "data_obj_name", parameter
           "report_ref" of type "data_obj_ref"
        """
        return self._client.run_job('kb_SetUtilities.KButil_Merge_FeatureSet_Collection',
                                    [params], self._service_ver, context)

    def KButil_Slice_FeatureSets_by_Genomes(self, params, context=None):
        """
        :param params: instance of type
           "KButil_Slice_FeatureSets_by_Genomes_Params"
           (KButil_Slice_FeatureSets_by_Genomes() ** **  Method for Slicing a
           FeatureSet or FeatureSets by a Genome, Genomes, or GenomeSet) ->
           structure: parameter "workspace_name" of type "workspace_name" (**
           The workspace object refs are of form: ** **    objects =
           ws.get_objects([{'ref':
           params['workspace_id']+'/'+params['obj_name']}]) ** ** "ref" means
           the entire name combining the workspace id and the object name **
           "id" is a numerical identifier of the workspace or object, and
           should just be used for workspace ** "name" is a string identifier
           of a workspace or object.  This is received from Narrative.),
           parameter "input_featureSet_refs" of type "data_obj_ref",
           parameter "input_genome_refs" of type "data_obj_ref", parameter
           "output_name" of type "data_obj_name", parameter "desc" of String
        :returns: instance of type
           "KButil_Slice_FeatureSets_by_Genomes_Output" -> structure:
           parameter "report_name" of type "data_obj_name", parameter
           "report_ref" of type "data_obj_ref"
        """
        return self._client.run_job('kb_SetUtilities.KButil_Slice_FeatureSets_by_Genomes',
                                    [params], self._service_ver, context)

    def KButil_Logical_Slice_Two_FeatureSets(self, params, context=None):
        """
        :param params: instance of type
           "KButil_Logical_Slice_Two_FeatureSets_Params"
           (KButil_Logical_Slice_Two_FeatureSets() ** **  Method for Slicing
           Two FeatureSets by Venn overlap) -> structure: parameter
           "workspace_name" of type "workspace_name" (** The workspace object
           refs are of form: ** **    objects = ws.get_objects([{'ref':
           params['workspace_id']+'/'+params['obj_name']}]) ** ** "ref" means
           the entire name combining the workspace id and the object name **
           "id" is a numerical identifier of the workspace or object, and
           should just be used for workspace ** "name" is a string identifier
           of a workspace or object.  This is received from Narrative.),
           parameter "input_featureSet_ref_A" of type "data_obj_ref",
           parameter "input_featureSet_ref_B" of type "data_obj_ref",
           parameter "operator" of String, parameter "desc" of String,
           parameter "output_name" of type "data_obj_name"
        :returns: instance of type
           "KButil_Logical_Slice_Two_FeatureSets_Output" -> structure:
           parameter "report_name" of type "data_obj_name", parameter
           "report_ref" of type "data_obj_ref"
        """
        return self._client.run_job('kb_SetUtilities.KButil_Logical_Slice_Two_FeatureSets',
                                    [params], self._service_ver, context)

    def KButil_Logical_Slice_Two_AssemblySets(self, params, context=None):
        """
        :param params: instance of type
           "KButil_Logical_Slice_Two_AssemblySets_Params"
           (KButil_Logical_Slice_Two_AssemblySets() ** **  Method for Slicing
           Two AssemblySets by Venn overlap) -> structure: parameter
           "workspace_name" of type "workspace_name" (** The workspace object
           refs are of form: ** **    objects = ws.get_objects([{'ref':
           params['workspace_id']+'/'+params['obj_name']}]) ** ** "ref" means
           the entire name combining the workspace id and the object name **
           "id" is a numerical identifier of the workspace or object, and
           should just be used for workspace ** "name" is a string identifier
           of a workspace or object.  This is received from Narrative.),
           parameter "input_assemblySet_ref_A" of type "data_obj_ref",
           parameter "input_assemblySet_ref_B" of type "data_obj_ref",
           parameter "operator" of String, parameter "desc" of String,
           parameter "output_name" of type "data_obj_name"
        :returns: instance of type
           "KButil_Logical_Slice_Two_AssemblySets_Output" -> structure:
           parameter "report_name" of type "data_obj_name", parameter
           "report_ref" of type "data_obj_ref"
        """
        return self._client.run_job('kb_SetUtilities.KButil_Logical_Slice_Two_AssemblySets',
                                    [params], self._service_ver, context)

    def KButil_Logical_Slice_Two_GenomeSets(self, params, context=None):
        """
        :param params: instance of type
           "KButil_Logical_Slice_Two_GenomeSets_Params"
           (KButil_Logical_Slice_Two_GenomeSets() ** **  Method for Slicing
           Two AssemblySets by Venn overlap) -> structure: parameter
           "workspace_name" of type "workspace_name" (** The workspace object
           refs are of form: ** **    objects = ws.get_objects([{'ref':
           params['workspace_id']+'/'+params['obj_name']}]) ** ** "ref" means
           the entire name combining the workspace id and the object name **
           "id" is a numerical identifier of the workspace or object, and
           should just be used for workspace ** "name" is a string identifier
           of a workspace or object.  This is received from Narrative.),
           parameter "input_genomeSet_ref_A" of type "data_obj_ref",
           parameter "input_genomeSet_ref_B" of type "data_obj_ref",
           parameter "operator" of String, parameter "desc" of String,
           parameter "output_name" of type "data_obj_name"
        :returns: instance of type
           "KButil_Logical_Slice_Two_GenomeSets_Output" -> structure:
           parameter "report_name" of type "data_obj_name", parameter
           "report_ref" of type "data_obj_ref"
        """
        return self._client.run_job('kb_SetUtilities.KButil_Logical_Slice_Two_GenomeSets',
                                    [params], self._service_ver, context)

    def KButil_Merge_GenomeSets(self, params, context=None):
        """
        :param params: instance of type "KButil_Merge_GenomeSets_Params"
           (KButil_Merge_GenomeSets() ** **  Method for merging GenomeSets)
           -> structure: parameter "workspace_name" of type "workspace_name"
           (** The workspace object refs are of form: ** **    objects =
           ws.get_objects([{'ref':
           params['workspace_id']+'/'+params['obj_name']}]) ** ** "ref" means
           the entire name combining the workspace id and the object name **
           "id" is a numerical identifier of the workspace or object, and
           should just be used for workspace ** "name" is a string identifier
           of a workspace or object.  This is received from Narrative.),
           parameter "input_refs" of type "data_obj_ref", parameter
           "output_name" of type "data_obj_name", parameter "desc" of String
        :returns: instance of type "KButil_Merge_GenomeSets_Output" ->
           structure: parameter "report_name" of type "data_obj_name",
           parameter "report_ref" of type "data_obj_ref"
        """
        return self._client.run_job('kb_SetUtilities.KButil_Merge_GenomeSets',
                                    [params], self._service_ver, context)

    def KButil_Build_GenomeSet(self, params, context=None):
        """
        :param params: instance of type "KButil_Build_GenomeSet_Params"
           (KButil_Build_GenomeSet() ** **  Method for creating a GenomeSet)
           -> structure: parameter "workspace_name" of type "workspace_name"
           (** The workspace object refs are of form: ** **    objects =
           ws.get_objects([{'ref':
           params['workspace_id']+'/'+params['obj_name']}]) ** ** "ref" means
           the entire name combining the workspace id and the object name **
           "id" is a numerical identifier of the workspace or object, and
           should just be used for workspace ** "name" is a string identifier
           of a workspace or object.  This is received from Narrative.),
           parameter "input_refs" of type "data_obj_ref", parameter
           "output_name" of type "data_obj_name", parameter "desc" of String
        :returns: instance of type "KButil_Build_GenomeSet_Output" ->
           structure: parameter "report_name" of type "data_obj_name",
           parameter "report_ref" of type "data_obj_ref"
        """
        return self._client.run_job('kb_SetUtilities.KButil_Build_GenomeSet',
                                    [params], self._service_ver, context)

    def KButil_Build_GenomeSet_from_FeatureSet(self, params, context=None):
        """
        :param params: instance of type
           "KButil_Build_GenomeSet_from_FeatureSet_Params"
           (KButil_Build_GenomeSet_from_FeatureSet() ** **  Method for
           obtaining a GenomeSet from a FeatureSet) -> structure: parameter
           "workspace_name" of type "workspace_name" (** The workspace object
           refs are of form: ** **    objects = ws.get_objects([{'ref':
           params['workspace_id']+'/'+params['obj_name']}]) ** ** "ref" means
           the entire name combining the workspace id and the object name **
           "id" is a numerical identifier of the workspace or object, and
           should just be used for workspace ** "name" is a string identifier
           of a workspace or object.  This is received from Narrative.),
           parameter "input_ref" of type "data_obj_ref", parameter
           "output_name" of type "data_obj_name", parameter "desc" of String
        :returns: instance of type
           "KButil_Build_GenomeSet_from_FeatureSet_Output" -> structure:
           parameter "report_name" of type "data_obj_name", parameter
           "report_ref" of type "data_obj_ref"
        """
        return self._client.run_job('kb_SetUtilities.KButil_Build_GenomeSet_from_FeatureSet',
                                    [params], self._service_ver, context)

    def KButil_Add_Genomes_to_GenomeSet(self, params, context=None):
        """
        :param params: instance of type
           "KButil_Add_Genomes_to_GenomeSet_Params"
           (KButil_Add_Genomes_to_GenomeSet() ** **  Method for adding a
           Genome to a GenomeSet) -> structure: parameter "workspace_name" of
           type "workspace_name" (** The workspace object refs are of form:
           ** **    objects = ws.get_objects([{'ref':
           params['workspace_id']+'/'+params['obj_name']}]) ** ** "ref" means
           the entire name combining the workspace id and the object name **
           "id" is a numerical identifier of the workspace or object, and
           should just be used for workspace ** "name" is a string identifier
           of a workspace or object.  This is received from Narrative.),
           parameter "input_genome_refs" of list of type "data_obj_ref",
           parameter "input_genomeset_ref" of type "data_obj_ref", parameter
           "output_name" of type "data_obj_name", parameter "desc" of String
        :returns: instance of type "KButil_Add_Genomes_to_GenomeSet_Output"
           -> structure: parameter "report_name" of type "data_obj_name",
           parameter "report_ref" of type "data_obj_ref"
        """
        return self._client.run_job('kb_SetUtilities.KButil_Add_Genomes_to_GenomeSet',
                                    [params], self._service_ver, context)

    def KButil_Remove_Genomes_from_GenomeSet(self, params, context=None):
        """
        :param params: instance of type
           "KButil_Remove_Genomes_from_GenomeSet_Params"
           (KButil_Remove_Genomes_from_GenomeSet() ** **  Method for removing
           Genomes from a GenomeSet) -> structure: parameter "workspace_name"
           of type "workspace_name" (** The workspace object refs are of
           form: ** **    objects = ws.get_objects([{'ref':
           params['workspace_id']+'/'+params['obj_name']}]) ** ** "ref" means
           the entire name combining the workspace id and the object name **
           "id" is a numerical identifier of the workspace or object, and
           should just be used for workspace ** "name" is a string identifier
           of a workspace or object.  This is received from Narrative.),
           parameter "input_genome_refs" of list of type "data_obj_ref",
           parameter "nonlocal_genome_names" of list of type "data_obj_name",
           parameter "input_genomeset_ref" of type "data_obj_ref", parameter
           "output_name" of type "data_obj_name", parameter "desc" of String
        :returns: instance of type
           "KButil_Remove_Genomes_from_GenomeSet_Output" -> structure:
           parameter "report_name" of type "data_obj_name", parameter
           "report_ref" of type "data_obj_ref"
        """
        return self._client.run_job('kb_SetUtilities.KButil_Remove_Genomes_from_GenomeSet',
                                    [params], self._service_ver, context)

    def KButil_Build_ReadsSet(self, params, context=None):
        """
        :param params: instance of type "KButil_Build_ReadsSet_Params"
           (KButil_Build_ReadsSet() ** **  Method for creating a ReadsSet) ->
           structure: parameter "workspace_name" of type "workspace_name" (**
           The workspace object refs are of form: ** **    objects =
           ws.get_objects([{'ref':
           params['workspace_id']+'/'+params['obj_name']}]) ** ** "ref" means
           the entire name combining the workspace id and the object name **
           "id" is a numerical identifier of the workspace or object, and
           should just be used for workspace ** "name" is a string identifier
           of a workspace or object.  This is received from Narrative.),
           parameter "input_refs" of type "data_obj_ref", parameter
           "output_name" of type "data_obj_name", parameter "desc" of String
        :returns: instance of type "KButil_Build_ReadsSet_Output" ->
           structure: parameter "report_name" of type "data_obj_name",
           parameter "report_ref" of type "data_obj_ref"
        """
        return self._client.run_job('kb_SetUtilities.KButil_Build_ReadsSet',
                                    [params], self._service_ver, context)

    def KButil_Merge_MultipleReadsSets_to_OneReadsSet(self, params, context=None):
        """
        :param params: instance of type
           "KButil_Merge_MultipleReadsSets_to_OneReadsSet_Params"
           (KButil_Merge_MultipleReadsSets_to_OneReadsSet() ** **  Method for
           merging multiple ReadsSets into one ReadsSet) -> structure:
           parameter "workspace_name" of type "workspace_name" (** The
           workspace object refs are of form: ** **    objects =
           ws.get_objects([{'ref':
           params['workspace_id']+'/'+params['obj_name']}]) ** ** "ref" means
           the entire name combining the workspace id and the object name **
           "id" is a numerical identifier of the workspace or object, and
           should just be used for workspace ** "name" is a string identifier
           of a workspace or object.  This is received from Narrative.),
           parameter "input_refs" of type "data_obj_ref", parameter
           "output_name" of type "data_obj_name", parameter "desc" of String
        :returns: instance of type
           "KButil_Merge_MultipleReadsSets_to_OneReadsSet_Output" ->
           structure: parameter "report_name" of type "data_obj_name",
           parameter "report_ref" of type "data_obj_ref"
        """
        return self._client.run_job('kb_SetUtilities.KButil_Merge_MultipleReadsSets_to_OneReadsSet',
                                    [params], self._service_ver, context)

    def KButil_Build_AssemblySet(self, params, context=None):
        """
        :param params: instance of type "KButil_Build_AssemblySet_Params"
           (KButil_Build_AssemblySet() ** **  Method for creating an
           AssemblySet) -> structure: parameter "workspace_name" of type
           "workspace_name" (** The workspace object refs are of form: ** ** 
           objects = ws.get_objects([{'ref':
           params['workspace_id']+'/'+params['obj_name']}]) ** ** "ref" means
           the entire name combining the workspace id and the object name **
           "id" is a numerical identifier of the workspace or object, and
           should just be used for workspace ** "name" is a string identifier
           of a workspace or object.  This is received from Narrative.),
           parameter "input_refs" of type "data_obj_ref", parameter
           "output_name" of type "data_obj_name", parameter "desc" of String
        :returns: instance of type "KButil_Build_AssemblySet_Output" ->
           structure: parameter "report_name" of type "data_obj_name",
           parameter "report_ref" of type "data_obj_ref"
        """
        return self._client.run_job('kb_SetUtilities.KButil_Build_AssemblySet',
                                    [params], self._service_ver, context)

    def KButil_Batch_Create_ReadsSet(self, params, context=None):
        """
        :param params: instance of type "KButil_Batch_Create_ReadsSet_Params"
           (KButil_Batch_Create_ReadsSet() ** **  Method for creating a
           ReadsSet without specifying individual objects) -> structure:
           parameter "workspace_name" of type "workspace_name" (** The
           workspace object refs are of form: ** **    objects =
           ws.get_objects([{'ref':
           params['workspace_id']+'/'+params['obj_name']}]) ** ** "ref" means
           the entire name combining the workspace id and the object name **
           "id" is a numerical identifier of the workspace or object, and
           should just be used for workspace ** "name" is a string identifier
           of a workspace or object.  This is received from Narrative.),
           parameter "name_pattern" of String, parameter "output_name" of
           type "data_obj_name", parameter "desc" of String
        :returns: instance of type "KButil_Batch_Create_ReadsSet_Output" ->
           structure: parameter "report_name" of type "data_obj_name",
           parameter "report_ref" of type "data_obj_ref"
        """
        return self._client.run_job('kb_SetUtilities.KButil_Batch_Create_ReadsSet',
                                    [params], self._service_ver, context)

    def KButil_Batch_Create_AssemblySet(self, params, context=None):
        """
        :param params: instance of type
           "KButil_Batch_Create_AssemblySet_Params"
           (KButil_Batch_Create_AssemblySet() ** **  Method for creating an
           AssemblySet without specifying individual objects) -> structure:
           parameter "workspace_name" of type "workspace_name" (** The
           workspace object refs are of form: ** **    objects =
           ws.get_objects([{'ref':
           params['workspace_id']+'/'+params['obj_name']}]) ** ** "ref" means
           the entire name combining the workspace id and the object name **
           "id" is a numerical identifier of the workspace or object, and
           should just be used for workspace ** "name" is a string identifier
           of a workspace or object.  This is received from Narrative.),
           parameter "name_pattern" of String, parameter "output_name" of
           type "data_obj_name", parameter "desc" of String
        :returns: instance of type "KButil_Batch_Create_AssemblySet_Output"
           -> structure: parameter "report_name" of type "data_obj_name",
           parameter "report_ref" of type "data_obj_ref"
        """
        return self._client.run_job('kb_SetUtilities.KButil_Batch_Create_AssemblySet',
                                    [params], self._service_ver, context)

    def KButil_Batch_Create_GenomeSet(self, params, context=None):
        """
        :param params: instance of type
           "KButil_Batch_Create_GenomeSet_Params"
           (KButil_Batch_Create_GenomeSet() ** **  Method for creating a
           GenomeSet without specifying individual objects) -> structure:
           parameter "workspace_name" of type "workspace_name" (** The
           workspace object refs are of form: ** **    objects =
           ws.get_objects([{'ref':
           params['workspace_id']+'/'+params['obj_name']}]) ** ** "ref" means
           the entire name combining the workspace id and the object name **
           "id" is a numerical identifier of the workspace or object, and
           should just be used for workspace ** "name" is a string identifier
           of a workspace or object.  This is received from Narrative.),
           parameter "name_pattern" of String, parameter "output_name" of
           type "data_obj_name", parameter "desc" of String
        :returns: instance of type "KButil_Batch_Create_GenomeSet_Output" ->
           structure: parameter "report_name" of type "data_obj_name",
           parameter "report_ref" of type "data_obj_ref"
        """
        return self._client.run_job('kb_SetUtilities.KButil_Batch_Create_GenomeSet',
                                    [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.run_job('kb_SetUtilities.status',
                                    [], self._service_ver, context)
